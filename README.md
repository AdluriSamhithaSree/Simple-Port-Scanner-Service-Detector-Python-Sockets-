# Simple Port Scanner & Service Detector

A lightweight open-source cybersecurity tool built using Python sockets.  
The tool scans a target IP address for open ports (1–1024) and identifies common services running on those ports.

## Features
- TCP port scanning using sockets  
- Identifies common services (HTTP, SSH, HTTPS, FTP, etc.)  
- Flags insecure services (Telnet, FTP, POP3)  
- Multi-threaded for fast scanning

## Use Case
Useful for:
- Basic reconnaissance during penetration testing
- Learning how port scanners work internally
- Identifying insecure services on networks

## Tech Stack
Python, Sockets, TCP/IP Networking

## Usage
python port_scanner.py
Enter Target IP: <IP_ADDRESS>

## Tech Stack
Python, Sockets, TCP/IP

## License
Open-source (MIT)
