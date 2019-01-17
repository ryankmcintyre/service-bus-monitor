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

# SAS Key
shared_access_key_name=os.environ['SAS_KEY_NAME']
shared_access_key_value=os.environ['SAS_KEY_VALUE']