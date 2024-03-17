1.cloud_login_activity.py:
# Cloud User Login Event Checker

This repository contains scripts to retrieve user login events from various cloud platforms: AWS, Azure, Google Cloud, and Oracle Cloud. These scripts provide functionality to monitor user login activities, including the IP address, login time, and duration of the session.

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
- For Azure script, you need to have an Azure subscription ID.

## Setup

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the cloned directory:

   ```bash
   cd cloud-user-login-event-checker
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use the scripts, navigate to the respective directory for the cloud provider you want to monitor and execute the Python script:

- **AWS:**
  
  ```bash
  cd aws
  python cloud_login_activity.py
  ```

- **Azure:**
  
  ```bash
  cd azure
  python cloud_login_activity.py
  ```

- **Google Cloud:**
  
  ```bash
  cd google_cloud
  python cloud_login_activity.py
  ```

- **Oracle Cloud:**
  
  ```bash
  cd oracle
  python cloud_login_activity.py
  ```
