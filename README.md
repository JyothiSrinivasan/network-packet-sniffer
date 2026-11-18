# Network Packet Sniffer

A beginner project for observing HTTP traffic on my own computer. The Scapy sniffer shows source and destination IP addresses and detects HTTP request lines. A separate test script sends sample requests and displays their response status.

## What it demonstrates

- Capturing packets with Python and Scapy
- Reading IPv4 source and destination addresses
- Identifying plain HTTP requests
- Comparing successful pages (200), missing pages (404), and timeouts

## Requirements

- Python
- Scapy: `pip install scapy`
- Npcap on Windows

## Run

Open two PowerShell windows in this project folder.

**Window 1 — start the sniffer:**

```powershell
python packet_sniffer.py
```

**Window 2 — send test requests:**

```powershell
python test_requests.py
```

Look at Window 1 for captured requests and Window 2 for HTTP status codes. Press **Ctrl+C** in Window 1 to stop capturing.

## Notes

The sniffer displays **requests**, while `test_requests.py` displays **response status codes**. A 404 request can still appear in the sniffer because the request reached the server.

This example examines plain HTTP traffic on port 80. It does not decrypt HTTPS traffic. If the sniffer selects the wrong network adapter, update its interface setting for your computer. Use it only on traffic you own or are authorized to inspect.