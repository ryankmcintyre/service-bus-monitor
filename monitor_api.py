import config, monitor_model, adal, requests
from msrestazure.azure_active_directory import AdalAuthentication
from msrestazure.azure_cloud import AZURE_PUBLIC_CLOUD

#TODO: Add check for existing non-expired token and don't get new one if not needed
def get_azure_token():
    LOGIN_ENDPOINT = AZURE_PUBLIC_CLOUD.endpoints.active_directory
    RESOURCE = "https://monitoring.azure.com/"

    context = adal.AuthenticationContext(LOGIN_ENDPOINT + '/' + config.tenant_id)
    credentials = AdalAuthentication(
        context.acquire_token_with_client_credentials,
        RESOURCE,
        config.client_id,
        config.client_password
    )
    return credentials



#strURL = "https://login.microsoftonline.com/##TENANTID##/oauth2/token"


def call_monitor_api(postData):
    apiUrl = f"https://{config.sb_region}.monitoring.azure.com{config.sb_resource_id}/metrics"
    #print(apiUrl)
    token = get_azure_token()
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}" 
    }
    
    print(token._args[2])
    #r = requests.post(apiUrl, data=postData, headers=headers)
    #print(r.text)

call_monitor_api(monitor_model.sample_metric())