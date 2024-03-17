from google.auth import default
from google.cloud import compute_v1

def check_firewall_rules():
    credentials, project_id = default()

    # Check if firewall rules are configured
    client = compute_v1.FirewallsClient(credentials=credentials)
    response = client.list(project=project_id)
    if not response:
        print("Firewall rules are not configured.")
        print("Recommendation: Configure firewall rules to control traffic to and from your Google Cloud resources.")
        print("How it protects: Firewall rules allow you to control inbound and outbound traffic, reducing the attack surface and protecting your resources.")

if __name__ == "__main__":
    check_firewall_rules()