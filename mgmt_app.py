from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.servicebus import ServiceBusManagementClient
import os, config

credentials = ServicePrincipalCredentials(
    client_id = config.client_id,
    secret = config.client_password,
    tenant = config.tenant_id
)

servicebus_mgmt_client = ServiceBusManagementClient(credentials, config.subscription_id)
sb_subscription = servicebus_mgmt_client.subscriptions.get(config.sb_resource_group, config.sb_namespace_name, config.sb_topic_name, config.sb_subscription_name)

print (sb_subscription.message_count, sb_subscription.count_details)