import oci
import datetime

def get_login_events():
    config = oci.config.from_file()
    identity_client = oci.identity.IdentityClient(config)

    now = datetime.datetime.utcnow()
    start_time = now - datetime.timedelta(hours=1)

    login_events = identity_client.list_auth_tokens(
        compartment_id=config['tenancy'],
        time_created_greater_than_or_equal_to=start_time
    )

    login_info = []
    for token in login_events.data:
        login_info.append({
            'User': token.user_name,
            'EventTime': token.time_created
        })

    return login_info

if __name__ == "__main__":
    login_info = get_login_events()
    for event in login_info:
        print(f"User: {event['User']} logged in at {event['EventTime']}")
