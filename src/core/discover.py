# File: src/core/discover.py

from scapy.all import srp, Ether, ARP
# Note: When running from the project root, the import will be different.
# For now, we'll import relative to its own folder for testing inside the VM.
from ..utils.db import setup_database, save_devices

def discover_devices(ip_range):
    """
    Discovers devices on the network using an ARP scan.
    """
    print(f"[*] Scanning for devices in {ip_range}...")
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
    # 1. Set up the database first
    print("[*] Initializing database...")
    # The DB file will be created relative to where you run the script.
    setup_database()
    
    # 2. Define the network range and run the scan
    # This is the range for your internal Hogwarts network
    network_range = "192.168.10.0/24" 
    found_devices = discover_devices(network_range)
    
    # 3. Save the results to the database
    if found_devices:
        print(f"[+] Found {len(found_devices)} devices. Saving to database...")
        save_devices(found_devices)
        print("[+] Database updated.")
    else:
        print("[-] No devices found.")
