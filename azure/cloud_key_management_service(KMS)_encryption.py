from azure.identity import DefaultAzureCredential
from azure.mgmt.keyvault import KeyVaultManagementClient

def check_key_vault_configuration():
    credential = DefaultAzureCredential()
    keyvault_client = KeyVaultManagementClient(credential, "<your_subscription_id>")

    # Check if Azure Key Vault is configured
    vaults = keyvault_client.vaults.list_all()
    if not vaults:
        print("Azure Key Vault is not configured.")
        print("Recommendation: Configure Azure Key Vault to centrally manage keys, secrets, and certificates.")
        print("How it protects: Azure Key Vault provides secure storage of keys and secrets, helping to safeguard your data.")

    # Check if encryption is enabled for services
    # Add your specific service checks here
    def check_key_vault_configuration():
    credential = DefaultAzureCredential()
    keyvault_client = KeyVaultManagementClient(credential, "<your_subscription_id>")

    # Check if Azure Key Vault is configured
    vaults = keyvault_client.vaults.list_all()
    if not vaults:
        print("Azure Key Vault is not configured.")
        print("Recommendation: Configure Azure Key Vault to centrally manage keys, secrets, and certificates.")
        print("How it protects: Azure Key Vault provides secure storage of keys and secrets, helping to safeguard your data.")

    # Check if encryption is enabled for specific services
    # Add your specific service checks here
    # For example, to check if Azure Storage encryption is enabled:
    storage_client = StorageManagementClient(credential, "<your_subscription_id>")
    accounts = storage_client.storage_accounts.list()
    for account in accounts:
        print(f"Storage Account: {account.name}")
        properties = storage_client.storage_accounts.get_properties(account.id)
        if not properties.encryption:
            print("Storage account encryption is not enabled.")
            print("Recommendation: Enable encryption for Azure Storage accounts to encrypt data at rest.")
            print("How it protects: Storage service encryption helps protect your data in Azure Storage by encrypting it before persisting it to disk.")

if __name__ == "__main__":
    check_key_vault_configuration()
