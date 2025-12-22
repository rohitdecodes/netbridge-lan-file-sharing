📡 NetBridge

Local-first File Sharing, Streaming & LAN Communication Tool

🔍 What is NetBridge?

NetBridge is a local-first network service that enables devices to share files, stream media, and communicate over a local network (LAN) without relying on cloud platforms or continuous internet connectivity.

It is designed to work in restricted or offline environments, and can optionally run over a VPN-based virtual LAN to extend access across distance while maintaining privacy.

🎯 Why NetBridge Was Built

Most modern file sharing solutions depend on:

Uploading files to the cloud

Internet connectivity

Public servers and storage duplication

NetBridge was built to explore an alternative approach:

Direct device-to-device access

Local networking instead of cloud dependency

Understanding how real networks behave in practice

The project prioritizes networking concepts and system behavior over complex application development.

⚙️ How NetBridge Works (High-Level)

NetBridge runs as a local server on a laptop or PC.

Other devices (mobiles or laptops) connect using the server’s IP address and port via a browser.

Files and media are accessed directly from the host device, without uploading to any third-party service.

Supported Network Modes

LAN (Wi-Fi / Hotspot / Ethernet) — works without internet

Bluetooth PAN — limited range, learning-oriented

VPN (ZeroTier) — virtual LAN over internet for extended distance

The same application works across all modes without code changes.

🌐 Networking Concepts Explored

This project helped in understanding:

Client–Server architecture

IP addressing (localhost vs 192.168.x.x vs 10.x.x.x)

Port-based services and access

NAT limitations and why public IP exposure often fails

VPNs as overlay (virtual) networks

Firewall behavior and access constraints

Local vs cloud trade-offs

🧠 Where NetBridge Is Useful (Use Cases)
1️⃣ Offline or Restricted Environments

College hostels and labs

Offices with blocked cloud services

Areas with unstable or no internet

2️⃣ Streaming Without File Duplication

Watch large videos directly from another device

Avoid downloading or copying files

Save storage space on mobile devices

3️⃣ Secure Local Sharing

Files remain inside the local or private network

No public exposure or third-party servers

Reduced attack surface

4️⃣ Learning & Demonstration

Practical understanding of LAN vs VPN

Demonstrating real-world networking constraints

Troubleshooting connectivity issues

🔐 VPN Mode (Optional)

NetBridge can operate over a VPN-based virtual LAN using tools like ZeroTier.

VPN creates a private network between devices

Devices behave as if they are on the same Wi-Fi network

Useful when devices are physically distant

Note:
VPN mode requires internet connectivity.
LAN mode works completely offline.


NetBridge is not intended to replace cloud platforms.

It is different because it:

Is local-first by design

Supports direct streaming, not just file transfer

Focuses on network behavior and architecture

Works across LAN and VPN without modification

Avoids public exposure intentionally

🧩 Is NetBridge “Better” Than Existing Tools?

No — and that is intentional.

NetBridge is not better for:

Global public sharing

Large-scale distribution

Cloud-based workflows

NetBridge is better suited for:

Local and private sharing

Learning networking concepts

Environments where cloud access is unnecessary or restricted

It solves a different problem.

⚠️ Disclaimer

This project was built with guided assistance to understand:

Networking fundamentals

System behavior

Real-world constraints

The primary focus was networking and architecture, not advanced software development or complex coding.

🛠 Technologies Used

Python (Flask)

Local Networking (LAN)

VPN (ZeroTier)

HTTP over private networks

📌 Project Status

Feature-complete for learning purposes

No plans for public exposure or cloud hosting

Intended as a networking / systems learning project

🧭 Key Takeaway

NetBridge is less about building an application and more about understanding how applications behave on real networks.

👤 Author

Built as a learning project focused on Networking, Cloud fundamentals, and System Design.
