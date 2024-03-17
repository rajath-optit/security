# Cloud Container Security Checker

This repository contains scripts to automate container security checks and implement best practices for container orchestration security using various cloud providers: AWS ECS, Azure AKS, Google GKE, and Oracle OKE.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
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
- For Azure scripts, you need to have an Azure subscription ID.
- For Oracle scripts, you need to have an Oracle Cloud Infrastructure account and OCI CLI configured.

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the cloned directory:

   ```bash
   cd Cloud-Container-Security-Checker
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the scripts, navigate to the respective directory for the cloud provider you want to check and execute the Python script:

- **AWS ECS:**
  
  ```bash
  cd aws
  python ecs_security_checker.py
  ```

- **Azure AKS:**
  
  ```bash
  cd azure
  python aks_security_checker.py
  ```

- **Google GKE:**
  
  ```bash
  cd google_cloud
  python gke_security_checker.py
  ```

- **Oracle OKE:**
  
  ```bash
  cd oracle
  python oke_security_checker.py
  ```
You can include this README.md file in your repository to provide users with instructions on how to set up and use the scripts for checking container security in various cloud environments. Adjust the content as needed to match your specific use case and environment.