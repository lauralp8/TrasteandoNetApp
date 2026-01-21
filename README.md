# NetApp Volume Management

A Python-based automation tool for managing NetApp storage volumes through the NetApp REST API.

## Overview

This project provides a streamlined interface for creating and managing NetApp storage volumes programmatically. It leverages the NetApp ONTAP REST API to perform volume operations, making it ideal for automated storage provisioning workflows.

## Features

- Automated volume creation on NetApp ONTAP clusters
- RESTful API integration with NetApp storage systems
- Configurable cluster connection settings
- Modular architecture for easy extension

## Project Structure

```
.
├── config.py           # Cluster configuration (hostname, credentials)
├── netapp_api.py       # NetApp API communication layer
├── create_volume.py    # Main volume creation script
├── requirements.txt    # Python package dependencies
└── README.md          # Project documentation
```

## Prerequisites

- Python 3.7 or higher
- Access to a NetApp ONTAP cluster
- Valid cluster credentials with appropriate permissions
- Network connectivity to the NetApp management interface

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd TrasteandoNetApp
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure cluster settings in `config.py`:
   - Update the cluster hostname/IP address
   - Set valid username and password
   - Adjust any additional configuration parameters

## Usage

Run the volume creation script:

```bash
python create_volume.py
```

Follow the prompts or modify the script to specify volume parameters such as:
- Volume name
- Size
- Aggregate
- Storage Virtual Machine (SVM)

## Configuration

### config.py

Contains essential cluster connection parameters:
- **Cluster hostname**: NetApp ONTAP cluster management IP or FQDN
- **Username**: Administrative user with volume creation privileges
- **Password**: Corresponding authentication credential

**Security Note**: Ensure `config.py` is added to `.gitignore` to prevent credential exposure.

## File Descriptions

| File | Purpose |
|------|---------|
| `config.py` | Configuration file for the cluster, user, and password |
| `netapp_api.py` | Functions to communicate with the NetApp API |
| `create_volume.py` | Main script to create a volume |
| `requirements.txt` | Python dependencies for the project |

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

[Specify your license here]

## Disclaimer

This tool is provided as-is for educational and automation purposes. Always test in a non-production environment before deploying to production systems.
