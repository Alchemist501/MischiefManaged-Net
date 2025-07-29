# File: src/core/discover.py

import logging
from scapy.all import srp, Ether, ARP
from ..utils.db import setup_database, save_devices
from ..utils.logger import setup_logger  # Import the new logger setup

# Set up the logger
logger = setup_logger()

def discover_devices(ip_range):
    """
    Discovers devices on the network using an ARP scan.
    """
    logger.info(f"Scanning for devices in {ip_range}...")
    arp_request = ARP(pdst=ip_range)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=2, verbose=False)[0]
    
    devices = []
    for sent, received in answered_list:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

# This part is for standalone testing.
if __name__ == "__main__":
    logger.info("Initializing database...")
    setup_database()
    
    network_range = "192.168.10.0/24" 
    found_devices = discover_devices(network_range)
    
    if found_devices:
        logger.info(f"Found {len(found_devices)} devices. Saving to database...")
        save_devices(found_devices)
        logger.info("Database updated.")
    else:
        logger.warning("No devices found.")