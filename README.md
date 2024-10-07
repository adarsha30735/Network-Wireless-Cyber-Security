![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
# Role of Blockchain to Improve Remote Healthcare System

## Overview
This project demonstrates how blockchain technology can enhance the security and privacy of remote healthcare systems. By leveraging blockchain, this system ensures a secure path for information sharing and verification across multiple layers, including local sensors, edge devices, fog servers, and medical servers. The diagnosis process is divided into three stages: initial diagnosis at the local device, intermediate diagnosis at the edge device, and final diagnosis at the medical server. This project integrates Insomnia API, Python, and Flask to model and showcase the blockchain-enabled healthcare system.

## Key Features
- **Multiple Layer Architecture**: Involves local devices, edge devices, fog servers, and medical servers for remote diagnosis and data transfer.
- **Blockchain Security**: Blockchain ensures secure and immutable medical data storage and transaction validation.
- **Medical Session Flow**: Tracks medical sessions from patient devices to cloud servers, ensuring data integrity and security at each step.
- **Machine Learning Integration**: Convolutional Neural Networks (CNNs) are used for intermediate diagnosis, such as arrhythmia detection from ECG signals.

## System Architecture
The system consists of multiple layers:
- **Local Device**: Attached to the patient, responsible for initial physiological data collection and preliminary diagnosis.
- **Edge Device**: Receives data from the local device, performs advanced analysis, and initiates communication with other nodes.
- **Fog Server**: Acts as an intermediary between edge devices and medical servers when there is poor connectivity.
- **Medical Server**: The final authority that verifies diagnoses and stores the final medical reports on the blockchain.

## Blockchain Workflow
The medical session is initiated by the local device, and data is passed through the layers, with blockchain used for secure verification and record storage. Each layer communicates and verifies the data using digital signatures, ensuring a secure flow of information.

## Core Algorithms
- **Local Device Diagnosis**: Detects abnormal ECG signals and sends them to the edge device.
- **Edge Device Verification**: Uses CNN classification to analyze the received data, broadcasting the session to other nodes for verification.
- **Medical Server Final Diagnosis**: Medical experts verify and update the final diagnosis results to the blockchain.

## Requirements
### Software Requirements:
- Python 3.x
- Flask
- Insomnia API (for API testing)
- Blockchain libraries (e.g., web3.py)
- Machine Learning libraries (e.g., TensorFlow, PyTorch for CNN)

# Project Code Files

This section lists the provided Python scripts and configuration files required for the implementation of the blockchain-enabled remote healthcare system.

## Provided Codes
The following Python scripts are part of the system's multi-layer architecture, consisting of the **Local Device**, **Edge Device**, and **Medical Server**.

### 1. `Edge_Device_2.py`
This script handles intermediate diagnosis and communication between local devices and fog servers or medical servers. It processes the data received from the local device, performs machine learning-based analysis, and relays the results for final verification.

### 2. `Local_Device_1.py`
This script is responsible for data collection from the patient, including physiological signals like ECG. It performs preliminary diagnosis and securely transmits the data to the edge device for further analysis.

### 3. `Medical_Server_3.py`
This script runs on the medical server, the final authority responsible for verifying diagnoses and updating patient records on the blockchain. It interacts with the blockchain to ensure that the data is securely stored and immutable.

## Configuration File
### 4. `devices.json`
This configuration file holds the necessary details about the devices in the system. It may include information such as:
- Device IDs
- IP addresses or network configurations
- Authentication tokens or digital certificates used for secure communication between layers

The JSON file is used to maintain an organized structure of device connections and their respective roles in the network.

## Subsection: Medical Blockchain Implementation

This subsection demonstrates the implementation of a blockchain for remote healthcare systems, using Flask for web interaction. The system uses blockchain to securely store and manage medical sessions across connected devices, ensuring data integrity and privacy.

### Key Features
- **Blockchain Construction**: Tracks medical sessions securely using cryptographic hashing.
- **Session Management**: Manages patient data, creates new sessions, and verifies the blockchain.
- **Device Connectivity**: Supports the addition of new devices to the network and synchronizes the blockchain across them.
- **Flask API**: Provides routes to interact with the blockchain for session retrieval, validation, and updates.

### Example Code
The following code snippet demonstrates how the blockchain is constructed and how the Flask API interacts with it.

```python
# Create a new session and add it to the blockchain
def create_session(self, previous_hash):
    session = {
        'session_index': len(self.virtualchain) + 1,
        'timestamp': str(datetime.datetime.now()),
        'previous_hash': previous_hash,
        'medical_sessions': self.medical_sessions
    }
    self.medical_sessions = []
    self.virtualchain.append(session)
    return session


## Installation
### Clone the repository:
```bash
git clone https://github.com/adarsha30735/Network-Wireless-Cyber-Security.git
