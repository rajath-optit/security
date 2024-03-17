from google.auth import default
from google.cloud import kms_v1

def check_kms_configuration():
    credentials, project_id = default()

    # Check if Google Cloud KMS key is configured
    client = kms_v1.KeyManagementServiceClient(credentials=credentials)
    keys = client.list_crypto_keys(parent=f"projects/{project_id}/locations/global")
    if not keys:
        print("Google Cloud KMS key is not configured.")
        print("Recommendation: Configure Google Cloud KMS key to encrypt data at rest.")
        print("How it protects: Google Cloud KMS provides a highly available and scalable key management solution.")

    # Check if encryption is enabled for services
    # Add your specific service checks here
    def check_kms_configuration():
    credentials, project_id = default()

    # Check if Google Cloud KMS key is configured
    client = kms_v1.KeyManagementServiceClient(credentials=credentials)
    keys = client.list_crypto_keys(parent=f"projects/{project_id}/locations/global")
    if not keys:
        print("Google Cloud KMS key is not configured.")
        print("Recommendation: Configure Google Cloud KMS key to encrypt data at rest.")
        print("How it protects: Google Cloud KMS provides a highly available and scalable key management solution.")

    # Check if encryption is enabled for specific services
    # Add your specific service checks here
    # For example, to check if Compute Engine disks are encrypted:
    compute_client = compute_v1.DisksClient(credentials=credentials)
    disks = compute_client.list(project=project_id, zone="your_zone")
    for disk in disks:
        print(f"Disk: {disk.name}")
        if not disk.disk_encryption_key:
            print("Disk encryption is not enabled.")
            print("Recommendation: Enable disk encryption for Compute Engine disks to encrypt data at rest.")
            print("How it protects: Disk encryption helps protect your data stored on Compute Engine disks by encrypting it before writing it to disk.")

if __name__ == "__main__":
    check_kms_configuration()

    