import oci

def check_network_security():
    config = oci.config.from_file()
    identity_client = oci.identity.IdentityClient(config)

    # Check if VCNs are configured
    vcns = identity_client.list_vcns(config["tenancy"]).data
    if not vcns:
        print("Virtual Cloud Networks (VCNs) are not configured.")
        print("Recommendation: Configure VCNs to isolate resources logically and control traffic flow.")
        print("How it protects: VCNs provide network isolation and control over traffic within the Oracle Cloud Infrastructure.")

if __name__ == "__main__":
    check_network_security()
