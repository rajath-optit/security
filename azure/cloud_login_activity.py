from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient
from datetime import datetime, timedelta

def get_login_events():
    credential = DefaultAzureCredential()
    monitor_client = MonitorManagementClient(credential, "<your_subscription_id>")

    filter_params = {
        "filter": "eventTimestamp ge {} and eventName eq 'SignInLogs'".format(
            (datetime.utcnow() - timedelta(days=1)).isoformat()
        )
    }

    login_events = monitor_client.activity_logs.list(filter_params)

    login_info = []
    for event in login_events:
        login_info.append({
            'User': event.caller,
            'EventTime': event.event_timestamp
        })

    return login_info

if __name__ == "__main__":
    login_info = get_login_events()
    for event in login_info:
        print(f"User: {event['User']} logged in at {event['EventTime']}")

///Note:
//Replace <your_subscription_id> with your Azure subscription ID in the Azure script.
//Ensure you have appropriate permissions and credentials configured to access the respective cloud provider's APIs.
//These scripts provide a starting point; you may need to adjust them based on your specific requirements and environment.///
