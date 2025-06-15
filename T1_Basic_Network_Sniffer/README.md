# 🕵️ Basic Packet Sniffer in Python

This project is a lightweight network packet sniffer written in Python. It captures raw network traffic at the Ethernet level and parses the data to reveal useful information about each packet.

## 🚀 Features

- Captures live packets directly from the network interface
- Extracts and displays:
  - Ethernet header details (source and destination MAC addresses)
  - Protocol type (IPv4 detection)
  - IPv4 header details: version, header length, source IP, destination IP, TTL, protocol type

## 🛠️ Requirements

- Python 3.x
- Linux or macOS (uses raw sockets via `AF_PACKET`)
- Root/Administrator privileges

## 📦 How to Run

### 1. Clone or download the project

```bash
git clone https://github.com/yourusername/basic-sniffer.git
cd basic-sniffer
