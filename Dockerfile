FROM python:3.7-alpine as base

FROM base as buildbase

RUN mkdir /install
WORKDIR /install

COPY requirements.txt ./

# Adding build dependencies first, also using cache-dir instead of --no-cache-dir due 
# to issue https://github.com/pypa/pip/issues/6158#issuecomment-456619072
RUN apk add --no-cache --virtual .cffi_deps build-base libffi-dev openssl-dev && \
    pip install --cache-dir=/pipcache --install-option="--prefix=/install" -r requirements.txt && \
    rm -rf /pipcache && \
    apk del .cffi_deps

FROM base

WORKDIR /usr/src/app

COPY --from=buildbase /install /usr/local
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
ENV METRIC_NAMESPACE=""

CMD [ "python3", "./mgmt_app.py" ]
