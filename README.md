# Service Bus Monitor
This project hooks up to Azure Service Bus and queries for subscription metrics, then sends those metrics to Azure Monitor using a [custom metric](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/metrics-custom-overview "Custom metric overview") where they can be used for reporting and alerts. Current metrics being sent are:
* Active Message Count
* Dead Letter Message Count

When specifying a Service Bus Namespace to query, all Topics on that namespace will be inspected and each Subscription on each Topic will have their metrics sent to Monitor.

The following environment variables must be set:
* SERVICEBUS_REGION - The Azure region where Service Bus is located (same region as Monitor, too)
* SERVICEBUS_RESOURCE_GROUP - Resource Group name
* SERVICEBUS_NAMESPACE_NAME - The Service Bus Namespace
* SAS_KEY_NAME - The name of a SAS key for Service Bus (only required to use app.py to send test messages)
* SAS_KEY_VALUE - The value of a SAS key for Service Bus (only required to use app.py to send test messages)
* SERVICEBUS_TOPIC_NAME - The name of a Topic to use when sending messages (only required when using app.py to send test messages)
* SERVICEBUS_SUBSCRIPTION_NAME - The name of a Subscription to use when receiving test messages (only required when using app.py to receive test messages)
* TENANT_ID - Tenant ID hosting the Azure resources
* CLIENT_ID - Azure AD Client ID for the application set up with "Contribute" and "Monitoring Metrics Publisher" on the Service Bus namespace
* CLIENT_PASSWORD - Azure AD Client Password for the application set up with "Contribute" and "Monitoring Metrics Publisher" on the Service Bus namespace
* SUBSCRIPTION_ID - Subscription ID hosting the Azure resources
* METRIC_NAMESPACE - Azure Monitor custom metric namespace name to use when sending metrics

A Dockerfile is included which can be used to create a container image. The image will execute mgmt_app.py using the above environment variables and output the result of the http post to Monitor.

The app.py file can be used for testing to send messages into Azure Service Bus, but is not used in the Dockerfile.