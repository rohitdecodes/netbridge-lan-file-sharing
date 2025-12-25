# NetBridge

## Overview
NetBridge is a local-first networking project that enables file sharing, media streaming,
and device communication over a Local Area Network (LAN) without relying on cloud platforms
or continuous internet connectivity.

The project is designed for restricted or offline environments and focuses on understanding
real-world networking behavior rather than building a large-scale application.

---

## Problem Statement
Most modern file-sharing and media streaming solutions depend on cloud infrastructure,
internet connectivity, and public servers. This creates limitations in environments where
internet access is restricted, unstable, or unnecessary.

There is a need to understand how direct device-to-device communication works using
local networking principles without relying on cloud services.

---

## Project Description
NetBridge operates as a local server running on a host device such as a laptop or PC.
Other devices connect to the server using the host’s IP address and port through a web browser.

Files and media are accessed directly from the host system without uploading data to
third-party platforms. The same application can operate across different network modes
without requiring changes to the core implementation.

The project prioritizes networking fundamentals, system behavior, and architectural
understanding over feature complexity.

---

## Key Features
- Local-first file sharing and media access
- Direct device-to-device communication
- No cloud dependency for LAN operation
- Browser-based client access
- Works across multiple network modes

---

## Supported Network Modes
- Local Area Network (Wi-Fi, Hotspot, Ethernet)
- Bluetooth Personal Area Network (learning-oriented)
- VPN-based Virtual LAN using ZeroTier

LAN mode works without internet connectivity.
VPN mode enables remote access by creating a virtual private network.

---

## Networking Concepts Explored
- Client–Server architecture
- IP addressing and private networks
- Port-based services
- Network Address Translation (NAT) behavior
- VPNs as overlay networks
- Firewall behavior and access control
- Local versus cloud networking trade-offs

---

## Use Cases
- File sharing in offline or restricted environments
- Media streaming without file duplication
- Secure sharing within a private network
- Learning and demonstration of real-world networking concepts

---

## Ethical Disclaimer
This project is developed strictly for educational and learning purposes.
It is intended to improve understanding of networking concepts and system behavior.
All demonstrations are performed with user awareness and informed consent.
The project follows ethical guidelines and responsible research practices.

---

## Technologies Used
- Python (Flask)
- Local Area Networking (LAN)
- VPN-based Virtual LAN (ZeroTier)
- HTTP over private networks

---

## Project Status
- Feature-complete for learning purposes
- No plans for public or cloud hosting
- Intended as a networking and systems learning project

---

## Learning Outcomes
- Practical understanding of LAN and VPN communication
- Exposure to real-world networking constraints
- Improved understanding of client-server systems
- Awareness of local versus cloud-based architectures

---

## Author
Built as a learning project focused on Networking, Cloud Fundamentals, and System Design.
