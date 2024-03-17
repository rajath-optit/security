import boto3

def check_security_groups():
    ec2 = boto3.client('ec2')
    
    # Check if security groups are configured
    response = ec2.describe_security_groups()
    if not response['SecurityGroups']:
        print("Security groups are not configured.")
        print("Recommendation: Configure security groups to control inbound and outbound traffic.")
        print("How it protects: Security groups act as virtual firewalls that control inbound and outbound traffic to AWS instances, enhancing network security.")

if __name__ == "__main__":
    check_security_groups()
