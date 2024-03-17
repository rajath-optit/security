import oci

def check_vault_configuration():
    config = oci.config.from_file()
    vault_client = oci.key_management.KmsVaultClient(config)

    # Check if Oracle Cloud Infrastructure Vault is configured
    vaults = vault_client.list_vaults(config["tenancy"])
    if not vaults.data:
        print("Oracle Cloud Infrastructure Vault is not configured.")
        print("Recommendation: Configure Oracle Cloud Infrastructure Vault to securely store and manage encryption keys.")
        print("How it protects: Oracle Cloud Infrastructure Vault provides a centralized solution for key management and encryption.")

    # Check if encryption is enabled for services
    # Add your specific service checks here
    def check_vault_configuration():
    config = oci.config.from_file()
    vault_client = oci.key_management.KmsVaultClient(config)

    # Check if Oracle Cloud Infrastructure Vault is configured
    vaults = vault_client.list_vaults(config["tenancy"])
    if not vaults.data:
        print("Oracle Cloud Infrastructure Vault is not configured.")
        print("Recommendation: Configure Oracle Cloud Infrastructure Vault to securely store and manage encryption keys.")
        print("How it protects: Oracle Cloud Infrastructure Vault provides a centralized solution for key management and encryption.")

    # Check if encryption is enabled for specific services
    # Add your specific service checks here
    # For example, to check if Object Storage encryption is enabled:
    object_storage_client = oci.object_storage.ObjectStorageClient(config)
    namespaces = object_storage_client.list_namespace()
    for namespace in namespaces:
        buckets = object_storage_client.list_buckets(namespace.name)
        for bucket in buckets:
            print(f"Bucket: {bucket.name}")
            if not bucket.default_s3_encryption_key:
                print("Object Storage bucket encryption is not enabled.")
                print("Recommendation: Enable server-side encryption for Object Storage buckets to encrypt data at rest.")
                print("How it protects: Server-side encryption helps protect your data stored in Object Storage by encrypting it before writing it to disk.")

if __name__ == "__main__":
    check_vault_configuration()
