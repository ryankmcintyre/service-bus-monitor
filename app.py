#! bin/python3.6

from azure.servicebus import ServiceBusService, Message, Topic
from azure.mgmt.servicebus import ServiceBusManagementClient
import os

service_namespace=os.environ['SERVICEBUS_NAMESPACE_NAME']
shared_access_key_name=os.environ['SAS_KEY_NAME']
shared_access_key_value=os.environ['SAS_KEY_VALUE']
topic = os.environ['SERVICEBUS_TOPIC_NAME']
subscription = os.environ['SERVICE_SUBSCRIPTION']

bus_service = ServiceBusService(
    service_namespace=service_namespace,
    shared_access_key_name=shared_access_key_name,
    shared_access_key_value=shared_access_key_value)

#msgSend = Message(b'Test Message3')
#bus_service.send_topic_message(topic, msgSend)

msg = bus_service.receive_subscription_message(topic, subscription, peek_lock=True)
print(msg.body)
msg.unlock

#bus_mgmt_service = ServiceBusManagementClient()
