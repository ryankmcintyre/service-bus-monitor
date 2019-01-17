#! bin/python3.6

from azure.servicebus import ServiceBusService, Message, Topic
from azure.mgmt.servicebus import ServiceBusManagementClient
import os, config

bus_service = ServiceBusService(
    service_namespace=config.sb_namespace_name,
    shared_access_key_name=config.shared_access_key_name,
    shared_access_key_value=config.shared_access_key_value)

msgSend = Message(b'Test Message3')
bus_service.send_topic_message(config.sb_topic_name, msgSend)

# msg = bus_service.receive_subscription_message(config.sb_topic_name, config.sb_subscription_name, peek_lock=True)
# print(msg.body)
# msg.unlock
