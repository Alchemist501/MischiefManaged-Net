# File: src/utils/db.py

import sqlite3
from datetime import datetime

# Define the database file path relative to the project root
DATABASE_FILE = "data/network_data.db"

def setup_database():
    """
    Sets up the database and creates the 'devices' table if it doesn't exist.
    """
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            mac TEXT PRIMARY KEY,
            ip TEXT,
            hostname TEXT,
            first_seen TEXT,
            last_seen TEXT
        )
        """)
        conn.commit()

def save_devices(devices_list):
    """
    Saves or updates a list of discovered devices in the database.
    
    Args:
        devices_list (list): A list of device dictionaries from the discovery scan.
    """
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        for device in devices_list:
            mac = device['mac']
            ip = device['ip']
            
            cursor.execute("SELECT * FROM devices WHERE mac=?", (mac,))
            result = cursor.fetchone()
            
            if result:
                # If it exists, update the last_seen time and IP
                cursor.execute("UPDATE devices SET last_seen=?, ip=? WHERE mac=?", (now, ip, mac))
            else:
                # If it's a new device, insert it
                cursor.execute("INSERT INTO devices (mac, ip, first_seen, last_seen) VALUES (?, ?, ?, ?)",
                               (mac, ip, now, now))
        conn.commit()
