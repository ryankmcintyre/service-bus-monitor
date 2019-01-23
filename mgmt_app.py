from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.servicebus import ServiceBusManagementClient
import os, config, json, monitor_model, datetime, monitor_api

credentials = ServicePrincipalCredentials(
    client_id = config.client_id,
    secret = config.client_password,
    tenant = config.tenant_id
)

# Grabbing the time now so we use the same timestamp for all metrics sent to monitor
query_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")

servicebus_mgmt_client = ServiceBusManagementClient(credentials, config.subscription_id)
sb_subscription = servicebus_mgmt_client.subscriptions.get(config.sb_resource_group, config.sb_namespace_name, config.sb_topic_name, config.sb_subscription_name)

#count_details = json.loads(sb_subscription.count_details.text)
#print (sb_subscription.message_count, sb_subscription.count_details)

def send_to_monitor_api(metric_name, metric_value):
    # Can't send zero, Monitor will return 400
    if metric_value == 0:
        return
    series = monitor_model.Series([config.sb_topic_name, config.sb_subscription_name], metric_value, metric_value, metric_value, 1) # Count always 1 since we're sending just one metric value
    baseData = monitor_model.BaseData(metric_name, "customnamespace", ["TopicName", "SubscriptionName"], [series])
    data = monitor_model.Data(baseData)
    azureMonitor = monitor_model.AzureMonitor(query_time, data)

    monitor_api.send_to_azure_monitor_api(json.dumps(azureMonitor, default=lambda o: o.__dict__))

# Currently only sending active_message_count and dead_letter_message_count
send_to_monitor_api("active_message_count", sb_subscription.count_details.active_message_count)
send_to_monitor_api("dead_letter_message_count", sb_subscription.count_details.dead_letter_message_count)
