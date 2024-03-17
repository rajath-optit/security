import boto3

def check_kms_configuration():
    client = boto3.client('kms')
    
    # Check if AWS KMS key is configured
    keys = client.list_keys()
    if not keys['Keys']:
        print("AWS KMS key is not configured.")
        print("Recommendation: Configure AWS KMS key to encrypt data at rest.")
        print("How it protects: AWS KMS provides a secure and durable solution for managing keys.")
    
    # Check if encryption is enabled for services
    # Add your specific service checks here
    def check_kms_configuration():
    client = boto3.client('kms')
    
    # Check if AWS KMS key is configured
    keys = client.list_keys()
    if not keys['Keys']:
        print("AWS KMS key is not configured.")
        print("Recommendation: Configure AWS KMS key to encrypt data at rest.")
        print("How it protects: AWS KMS provides a secure and durable solution for managing keys.")
    
    # Check if encryption is enabled for specific services
    # Add your specific service checks here
    # For example, to check if S3 buckets are encrypted:
    s3 = boto3.client('s3')
    response = s3.get_bucket_encryption(Bucket='your_bucket_name')
    if 'ServerSideEncryptionConfiguration' not in response:
        print("S3 bucket encryption is not enabled.")
        print("Recommendation: Enable server-side encryption for S3 buckets to encrypt data at rest.")
        print("How it protects: Server-side encryption helps protect your data stored in S3 by encrypting it before writing it to disk.")

if __name__ == "__main__":
    check_kms_configuration()

