# File: src/core/sniffer.py

from scapy.all import sniff, IP, TCP, UDP, ICMP
from ..utils.logger import setup_logger
from ..utils.db import save_network_event  # <-- Import the new function
from datetime import datetime

logger = setup_logger()

def packet_callback(packet):
    if IP not in packet:
        return

    event = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "src_ip": packet[IP].src,
        "dst_ip": packet[IP].dst,
        "protocol": None, "src_port": None, "dst_port": None,
        "packet_size": len(packet)
    }

    if TCP in packet:
        event.update({
            "protocol": "TCP",
            "src_port": packet[TCP].sport,
            "dst_port": packet[TCP].dport
        })
    elif UDP in packet:
        event.update({
            "protocol": "UDP",
            "src_port": packet[UDP].sport,
            "dst_port": packet[UDP].dport
        })
    elif ICMP in packet:
        event["protocol"] = "ICMP"
    else:
        event["protocol"] = packet[IP].proto

    # Log to console AND save to database
    logger.info(f"Captured {event['protocol']} Packet: {event['src_ip']} -> {event['dst_ip']}")
    save_network_event(event)

def start_sniffing(interface=None):
    logger.info("Starting packet sniffer... Press Ctrl+C to stop.")
    sniff(iface=interface, prn=packet_callback, store=False)

if __name__ == "__main__":
    start_sniffing(interface="eth0")