import config, monitor_model, adal, requests, json, time
from msrestazure.azure_active_directory import AdalAuthentication
from msrestazure.azure_cloud import AZURE_PUBLIC_CLOUD

def get_local_token():
    try:
        with open("token.json", "r") as infile:
            token = json.load(infile)
            if int(token["expires_on"]) < int(time.time()): # Token expired
                return
            else:
                return(token["access_token"])
    except FileNotFoundError: # Sorry, no local token
        return

def get_azure_token():
    LOGIN_ENDPOINT = AZURE_PUBLIC_CLOUD.endpoints.active_directory
    RESOURCE = "https://monitoring.azure.com/"

    token = get_local_token()

    if token:
        return token
    else:
        # Tried using the SDK to get a token for the API call but didn't figure out how to use it, so 
        # switched to the HTTP method
        # ----------------------------------
        # context = adal.AuthenticationContext(LOGIN_ENDPOINT + '/' + config.tenant_id)
        # credentials = AdalAuthentication(
        #     context.acquire_token_with_client_credentials,
        #     RESOURCE,
        #     config.client_id,
        #     config.client_password
        # )
        # return credentials

        login_url = f"{LOGIN_ENDPOINT}/{config.tenant_id}/oauth2/token"
        form_data = {
            "grant_type": "client_credentials",
            "client_id": config.client_id,
            "client_secret": config.client_password,
            "resource": RESOURCE
        }

        resp = requests.post(login_url, data=form_data)
        resp_json = json.loads(resp.text)
        # Save locally for reuse
        with open("token.json", "w") as outfile:
            json.dump(resp_json, outfile)
        
        return resp_json["access_token"]

def send_to_azure_monitor_api(postData):
    apiUrl = f"https://{config.sb_region}.monitoring.azure.com/subscriptions/{config.subscription_id}/resourceGroups/{config.sb_resource_group}/providers/Microsoft.ServiceBus/namespaces/{config.sb_namespace_name}/metrics"
    
    token = get_azure_token()
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}" 
    }
    
    r = requests.post(apiUrl, data=postData, headers=headers)
    print(r.status_code)

#send_to_azure_monitor_api(monitor_model.sample_metric())