from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.servicebus import ServiceBusManagementClient
import os

# Tenant ID & Subscription ID for your Azure Subscription
tenant_id = os.environ['TENANT_ID']
subscription_id = os.environ['SUBSCRIPTION_ID']

# Your Service Principal App ID
client_id = os.environ['CLIENT_ID']

# Your Service Principal Password
client_password = os.environ['CLIENT_PASSWORD']

# Service Bus Details
sb_resource_group = os.environ['SERVICEBUS_RESOURCE_GROUP']
sb_namespace_name = os.environ['SERVICEBUS_NAMESPACE_NAME']
sb_topic_name = os.environ['SERVICEBUS_TOPIC_NAME']
sb_subscription_name = os.environ['SERVICEBUS_SUBSCRIPTION_NAME']

#print("client: " + client_id, "clientSecret: " + client_password, "tenant:" + tenant_id)

credentials = ServicePrincipalCredentials(
    client_id = client_id,
    secret = client_password,
    tenant = tenant_id
)

servicebus_mgmt_client = ServiceBusManagementClient(credentials, subscription_id)
sb_subscription = servicebus_mgmt_client.subscriptions.get(sb_resource_group, sb_namespace_name, sb_topic_name, sb_subscription_name)

print (sb_subscription.message_count, sb_subscription.count_details)

