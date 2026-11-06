# Network Reconnaissance Toolkit

A beginner-friendly Python cybersecurity project focused on network reconnaissance and TCP port scanning.

This project was created to develop practical Python programming skills and understand the fundamentals of network reconnaissance.

## Features

- **IP Address Validation** – Validates IPv4 and IPv6 addresses.
- **Hostname Validation** – Checks whether a hostname can be resolved to an IPv4 address.
- **Network Calculation** – Uses Python's `ipaddress` module to calculate network information.
- **Host Discovery** – Includes a helper function for checking host availability using ICMP ping.
- **TCP Port Scanning** – Checks selected TCP ports using Python sockets.
- **Port Status Classification** – Categorizes ports as open, closed, filtered/unknown, or unknown.
- **Scan Summary** – Displays the total number of ports in each status category.

*Note: Network calculation and host discovery functions are implemented but are not yet integrated into the main program workflow.*


## Ports Scanned

The current version checks these TCP ports:

| Port | Common Service |
|---|---|
| 22 | SSH |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 465 | SMTP over TLS |
| 143 | IMAP |
| 69 | TFTP (UDP, not scanned by this TCP tool) |
| 23 | Telnet |
| 25 | SMTP |
| 8080 | HTTP Alternative |

**Note:** Port 69 is included in the list, but this version performs TCP scanning only. TFTP normally uses UDP.

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open the project folder in your terminal.
4. Run:

```bash
python3 main1.py
```

5. Enter an IP address or hostname when prompted.

Only scan devices and networks that you own or have explicit permission to test.

## Development Roadmap

Planned improvements:

- [ ] Custom port selection
- [ ] DNS and service discovery
- [ ] Improved scan reporting
- [ ] Device identification
- [ ] IoT device reconnaissance
- [ ] Additional network reconnaissance features

## Version

**Version 1.0 — Initial Release**

This is an ongoing learning project. New features and improvements will be added in future versions.
