import boto3
from datetime import datetime, timedelta

def get_login_events(start_time=None, end_time=None):
    try:
        client = boto3.client('cloudtrail')
        
        # Set default time range if not provided
        if not start_time:
            start_time = datetime.now() - timedelta(days=1)
        if not end_time:
            end_time = datetime.now()

        # Convert datetime objects to ISO 8601 format string
        start_time_str = start_time.isoformat()
        end_time_str = end_time.isoformat()

        response = client.lookup_events(
            LookupAttributes=[
                {
                    'AttributeKey': 'EventName',
                    'AttributeValue': 'ConsoleLogin'
                }
            ],
            StartTime=start_time_str,
            EndTime=end_time_str
        )

        login_events = []
        for event in response['Events']:
            login_events.append({
                'User': event['Username'],
                'EventTime': event['EventTime'],
                'IPAddress': event.get('SourceIPAddress', 'N/A'),
                'UserAgent': event.get('UserAgent', 'N/A')
            })

        return login_events

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

if __name__ == "__main__":
    # Example usage: Retrieve login events for the last 24 hours
    start_time = datetime.now() - timedelta(days=1)
    end_time = datetime.now()
    login_events = get_login_events(start_time, end_time)
    
    if login_events:
        for event in login_events:
            print(f"User: {event['User']} logged in at {event['EventTime']} from IP: {event['IPAddress']} using: {event['UserAgent']}")
    else:
        print("No login events found.")
