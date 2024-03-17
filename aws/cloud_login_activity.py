import boto3

def get_login_events():
    client = boto3.client('cloudtrail')

    response = client.lookup_events(
        LookupAttributes=[
            {
                'AttributeKey': 'EventName',
                'AttributeValue': 'ConsoleLogin'
            }
        ]
    )

    login_events = []
    for event in response['Events']:
        login_events.append({
            'User': event['Username'],
            'EventTime': event['EventTime']
        })

    return login_events

if __name__ == "__main__":
    login_events = get_login_events()
    for event in login_events:
        print(f"User: {event['User']} logged in at {event['EventTime']}")
