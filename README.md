# Network Security Scanner

## Overview

This **Basic Network Security Scanner** is a simple tool for scanning open ports and testing if a given target is online using basic ICMP (ping) and TCP port scanning methods.

## Features

- **ICMP Ping**: Checks if the target IP is online.
- **TCP Port Scan**: Scans for open ports within a given range (default: ports 1-1024).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Talhanaeem396/Network-Security-Scanner.git

2. Navigate to the project directory:
   ```bash
   cd network-security-scanner

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt


## Usage
To start a scan, run the script and enter the target IP when prompted:
   ```bash
   python network_scanner.py

## Example Output:
Enter the IP address to scan: 192.168.1.1
Pinging 192.168.1.1...
Scanning ports on 192.168.1.1...
Open ports on 192.168.1.1: [22, 80, 443]
Network security scan for 192.168.1.1 completed.

## Dependencies
The required Python libraries are listed in the requirements.txt file.
