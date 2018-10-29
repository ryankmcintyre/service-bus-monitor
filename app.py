#! bin/python3.6

from azure.servicebus import ServiceBusService, Message, Topic
import os

service_namespace=os.environ['SERVICE_NAMESPACE']
shared_access_key_name=os.environ['SAS_KEY_NAME']
shared_access_key_value=os.environ['SAS_KEY_VALUE']
topic = os.environ['SERVICE_TOPIC']
subscription = os.environ['SERVICE_SUBSCRIPTION']

bus_service = ServiceBusService(
    service_namespace=service_namespace,
    shared_access_key_name=shared_access_key_name,
    shared_access_key_value=shared_access_key_value)

msg = bus_service.receive_subscription_message(topic, subscription, peek_lock=True)
print(msg.body)
