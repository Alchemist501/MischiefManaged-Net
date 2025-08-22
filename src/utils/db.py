# File: src/utils/db.py

import sqlite3
from datetime import datetime

DATABASE_FILE = "data/network_data.db"

def setup_database():
    """Sets up the database and creates tables if they don't exist."""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        
        # devices table (no changes here)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            mac TEXT PRIMARY KEY, ip TEXT, hostname TEXT,
            first_seen TEXT, last_seen TEXT
        )""")
        
        # NEW: network_events table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS network_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            src_ip TEXT,
            dst_ip TEXT,
            protocol TEXT,
            src_port INTEGER,
            dst_port INTEGER,
            packet_size INTEGER
        )""")
        conn.commit()

# save_devices function (no changes here)
def save_devices(devices_list):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for device in devices_list:
            mac, ip = device['mac'], device['ip']
            cursor.execute("SELECT * FROM devices WHERE mac=?", (mac,))
            if cursor.fetchone():
                cursor.execute("UPDATE devices SET last_seen=?, ip=? WHERE mac=?", (now, ip, mac))
            else:
                cursor.execute("INSERT INTO devices (mac, ip, first_seen, last_seen) VALUES (?, ?, ?, ?)",
                               (mac, ip, now, now))
        conn.commit()

# NEW: Function to save a single network event
def save_network_event(event_data):
    """Saves a single network event to the database."""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO network_events (timestamp, src_ip, dst_ip, protocol, src_port, dst_port, packet_size)
        VALUES (:timestamp, :src_ip, :dst_ip, :protocol, :src_port, :dst_port, :packet_size)
        """, event_data)
        conn.commit()

def get_all_devices():
    """Retrieves all devices from the database."""
    with sqlite3.connect(DATABASE_FILE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM devices ORDER BY last_seen DESC")
        devices = [dict(row) for row in cursor.fetchall()]
        return devices