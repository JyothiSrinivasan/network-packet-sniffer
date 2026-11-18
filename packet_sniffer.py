from scapy.all import IP, TCP, Raw, sniff, conf

HTTP_METHODS = (
    b"GET ", b"POST ", b"PUT ", b"DELETE ",
    b"HEAD ", b"OPTIONS ", b"PATCH ",
)


def check_packet(packet):
    # We need IP addresses, TCP information, and actual packet content.
    if not (IP in packet and TCP in packet and Raw in packet):
        return

    content = bytes(packet[Raw].load)

    # The first line of an HTTP request starts with a method.
    if not content.startswith(HTTP_METHODS):
        return

    first_line = content.split(b"\r\n", 1)[0]
    request = first_line.decode("ascii", errors="replace")

    print(
        f"HTTP request | {packet[IP].src} → {packet[IP].dst} "
        f"| {request}"
    )


print("Watching HTTP traffic on TCP port 80. Press Ctrl+C to stop.")

try:
    sniff(
        iface=conf.ifaces.dev_from_index(12),
        filter="tcp port 80",
        prn=check_packet,
        store=False,
    )
except KeyboardInterrupt:
    print("\nCapture stopped.")