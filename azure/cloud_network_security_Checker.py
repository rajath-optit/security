from azure.identity import DefaultAzureCredential
from azure.mgmt.network import NetworkManagementClient

def check_network_security_groups():
    credential = DefaultAzureCredential()
    network_client = NetworkManagementClient(credential, "<your_subscription_id>")

    # Check if network security groups are configured
    nsgs = list(network_client.network_security_groups.list_all())
    if not nsgs:
        print("Network security groups are not configured.")
        print("Recommendation: Configure network security groups to filter traffic at the network level.")
        print("How it protects: Network security groups act as firewalls, allowing or denying traffic to and from Azure resources based on rules you define.")

if __name__ == "__main__":
    check_network_security_groups()
