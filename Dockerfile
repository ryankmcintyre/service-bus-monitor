FROM python:3.6

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Environment variables
ENV SERVICE_NAMESPACE="rkmtest"
ENV SAS_KEY_NAME="listen"
ENV SAS_KEY_VALUE=""
ENV SERVICE_TOPIC="test"
ENV SERVICE_SUBSCRIPTION="test-sub"

CMD [ "python3", "./app.py" ]
