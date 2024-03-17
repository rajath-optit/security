from google.auth import default
from google.auth.transport.requests import Request
from google.cloud import logging_v2

def get_login_events():
    credentials, project_id = default()

    client = logging_v2.LoggingServiceV2Client(credentials=credentials)

    filter_str = 'resource.type="audited_resource" AND log_name="activity" AND protoPayload.methodName="google.cloud.audit.v1.LogEntry.Action.Login"'

    response = client.list_log_entries(
        resource_names=[f"projects/{project_id}"],
        filter_=filter_str,
        order_by="timestamp desc",
        page_size=10
    )

    login_events = []
    for entry in response:
        login_events.append({
            'User': entry.proto_payload.authentication_info.principal_email,
            'EventTime': entry.timestamp
        })

    return login_events

if __name__ == "__main__":
    login_events = get_login_events()
    for event in login_events:
        print(f"User: {event['User']} logged in at {event['EventTime']}")
