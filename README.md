# Network Automation Project

## Overview

This repository focuses on **network automation** using Python, implementing features like **multithreading** and **asynchronous command execution** to efficiently manage multiple devices. The project is designed to automate complex tasks on network devices, including executing commands across multiple devices in parallel, managing playbooks with dependent command sets, and troubleshooting network issues.

## Features

- **Multithreading & Asynchronous Execution**: Efficiently handle multiple device connections and command execution in parallel.
- **Playbook Management**: Create, store, and load playbooks to execute complex, dependent command sets across devices.
- **Linux Iptables Automation**: Automate firewall configurations and rules on Linux machines.
- **Project Management & Troubleshooting**: Focus on building robust, scalable solutions for multi-device management and troubleshooting network-related issues.

## Technologies

- **Python**: Core language for automation.
- **Paramiko**: For SSH-based communication with network devices.
- **AsyncSSH**: To handle asynchronous communication for larger networks.
- **Multithreading**: For concurrent execution of commands on multiple devices.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/network-automation.git
   cd network-automation
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Example of Running the Script

1. Edit the `devices` and `commands` list in the script to match your network setup.

2. Run the `main.py` file:
   ```bash
   python main.py
   ```

3. Choose from the menu options to create, load, or execute a playbook.

## Project Structure

```
.
├── main.py               # Entry point to the project
├── ssh_manager.py        # Handles SSH connections and multithreading
├── utils.py              # Utility functions for various operations
├── playbooks/            # Directory to store and manage playbooks
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

## Playbooks

Playbooks allow you to group dependent commands to be executed across multiple devices. You can create, load, and manage playbooks through the command-line interface provided by this project.

## Future Improvements

- **Enhance Playbook Compatibility**: Extend support to more device types for broader compatibility.
- **Improve Visual Presentation**: Add better logging and visualization to track command execution in real-time.
- **Scalability Enhancements**: Optimize the project for larger networks with hundreds of devices.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue if you'd like to collaborate.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
