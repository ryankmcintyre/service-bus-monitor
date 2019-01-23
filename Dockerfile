FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Environment variables
ENV SERVICEBUS_REGION=""
ENV SERVICEBUS_RESOURCE_GROUP=""
ENV SERVICEBUS_NAMESPACE_NAME=""
ENV SERVICEBUS_RESOURCE_ID=""
ENV SAS_KEY_NAME=""
ENV SAS_KEY_VALUE=""
ENV SERVICEBUS_TOPIC_NAME=""
ENV SERVICEBUS_SUBSCRIPTION_NAME=""
ENV TENANT_ID=""
ENV CLIENT_ID=""
ENV CLIENT_PASSWORD=""
ENV SUBSCRIPTION_ID=""

CMD [ "python3", "./mgmt_app.py" ]
