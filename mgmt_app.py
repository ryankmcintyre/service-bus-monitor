# This uses coroutines available in the asyncio module in Python 3.7+
# https://docs.python.org/3/library/asyncio-task.html#awaitables
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.servicebus import ServiceBusManagementClient
import asyncio, os, config, json, monitor_model, datetime, monitor_api

# Grabbing the time now so we use the same timestamp for all metrics sent to monitor
query_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")

def send_to_monitor_api(topic_name, subscription_name, metric_name, metric_value):
    # Can't send zero, Monitor will return 400
    if metric_value == 0:
        return
    series = monitor_model.Series([topic_name, subscription_name], metric_value, metric_value, metric_value, 1) # Count always 1 since we're sending just one metric value
    baseData = monitor_model.BaseData(metric_name, config.metric_namespace, ["TopicName", "SubscriptionName"], [series])
    data = monitor_model.Data(baseData)
    azureMonitor = monitor_model.AzureMonitor(query_time, data)
    print("Sending", topic_name, subscription_name, metric_name, metric_value)
    monitor_api.send_to_azure_monitor_api(json.dumps(azureMonitor, default=lambda o: o.__dict__))

async def send_subscription_metrics(servicebus_mgmt_client, topic_name):
    subscriptions = servicebus_mgmt_client.subscriptions.list_by_topic(config.sb_resource_group, config.sb_namespace_name, topic_name)
    for subscription in subscriptions:
        send_to_monitor_api(
            topic_name,
            subscription.name,
            "active_message_count",
            subscription.count_details.active_message_count
        )
        send_to_monitor_api(
            topic_name,
            subscription.name,
            "dead_letter_message_count",
            subscription.count_details.dead_letter_message_count
        )

async def main():
    # Parameters for an Azure AD Application that has permission for
    # "Contributor" and "Monitoring Metrics Publisher" on the Service Bus Namespace
    credentials = ServicePrincipalCredentials(
        client_id = config.client_id,
        secret = config.client_password,
        tenant = config.tenant_id
    )

    servicebus_mgmt_client = ServiceBusManagementClient(credentials, config.subscription_id)

    topics = servicebus_mgmt_client.topics.list_by_namespace(config.sb_resource_group, config.sb_namespace_name)
    # Gather and send metrics for each topic in an async manner.
    for topic in topics:
        asyncio.create_task(send_subscription_metrics(servicebus_mgmt_client, topic.name))


if __name__ == "__main__":
    # Run the main func and wait until we're done.
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())