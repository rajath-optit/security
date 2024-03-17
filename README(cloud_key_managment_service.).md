# Cloud Data Encryption Checker

This repository contains scripts to check data encryption configurations across various cloud platforms: AWS, Azure, Google Cloud, and Oracle Cloud. These scripts help identify if data encryption at rest and in transit measures are properly configured using services like AWS KMS, Azure Key Vault, Google Cloud KMS, and Oracle Cloud Infrastructure Vault.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before using the scripts, ensure you have the following prerequisites:

- Python 3.x installed on your system.
- Required Python packages installed. You can install them using `pip`:

  ```bash
  pip install -r requirements.txt
  ```

- Proper access credentials and permissions configured for accessing cloud APIs.
- For the Azure script, you need to have an Azure subscription ID.

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the cloned directory:

   ```bash
   cd Cloud-Data-Encryption-Checker
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the scripts, navigate to the respective directory for the cloud provider you want to check and execute the Python script:

- **AWS:**
  
  ```bash
  cd aws
  python cloud_data_encryption_checker.py
  ```

- **Azure:**
  
  ```bash
  cd azure
  python cloud_data_encryption_checker.py
  ```

- **Google Cloud:**
  
  ```bash
  cd google_cloud
  python cloud_data_encryption_checker.py
  ```

- **Oracle Cloud:**
  
  ```bash
  cd oracle
  python cloud_data_encryption_checker.py
  ```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

This README provides instructions on setting up, using, and contributing to the Cloud Data Encryption Checker repository. Users can follow these guidelines to utilize the provided scripts effectively.