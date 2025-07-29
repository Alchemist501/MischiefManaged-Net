# 🗺️ The Marauder's Map: Personal Network Sentinel

> _"Mischief Managed." Beyond the visible network. This Python project meticulously traces the faint digital whispers and hidden connections on your network, revealing the true nature of every footprint. What secrets does your silence hold?_

---

## ✨ Project Overview

Inspired by the magical Marauder's Map from the wizarding world, this project is a **personal network reconnaissance and anomaly detection system**. It brings clarity and security to your local network by:

- Continuously monitoring activity
- Identifying connected devices
- Flagging suspicious behaviors

Think of it as your personal digital sentinel, ensuring no "unregistered animagi" or "Dark Arts" go unnoticed on your Wi-Fi.

> **Note:** This is a solo project to demonstrate practical skills in network security, data analysis, and software development.

---

## 🚀 Features

### **Current Capabilities (Phase 1)**

- **Network Device Discovery:**  
   Automatically scans your local network to identify all active devices, capturing their IP and MAC addresses ("footprints").
- **Basic Packet Sniffing:**  
   Captures live network traffic flowing through your system's interface.
- **Structured Data Storage:**  
   Logs all discovered devices and parsed network activity into a local SQLite database for persistent record-keeping.
- **Basic Logging:**  
   Implements robust logging to track script activities, discoveries, and potential issues.

### **Planned Features (Future Phases)**

- **Interactive Network Map Visualization:**  
   Web-based graphical representation of connected devices and their communication pathways.
- **Basic Anomaly Detection:**  
   Rule-based/statistical methods to flag unusual network behaviors (e.g., new/unknown devices, excessive traffic, suspicious port activity).
- **Alert Generation:**  
   Real-time notifications for detected anomalies.
- **Historical Activity Review:**  
   Query and visualize past network activity and alerts.
- **Device Fingerprinting:**  
   Infer device types/manufacturers from MAC addresses (OUI lookup).

---

## 🛠️ Technologies Used

- **Python 3.x:** Primary programming language
- **Scapy:** Network packet crafting and sniffing
- **SQLite:** Lightweight, file-based database
- **Flask:** _(Planned)_ Backend API
- **JavaScript, HTML, CSS:** _(Planned)_ Frontend development
- **Vis.js / Cytoscape.js / D3.js:** _(Planned)_ Network graph visualization

---

## ⚡ Getting Started

### **Prerequisites**

- Python 3.x
- `pip` (Python package installer)
- `git`

### **Setup & Installation**

1. **Clone the repository:**

   ```bash
   git clone github.com/Alchemist501/MischiefManaged-Net.git
   cd MischiefManaged-Net
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   ```

   - **On Windows:**
     ```bash
     .\venv\Scripts\activate
     ```
   - **On macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install scapy
   pip install SQLAlchemy  # For database interaction
   ```

---

## ▶️ Usage (Phase 1: Device Discovery & Basic Packet Sniffing)

Easily get started with the core features! Make sure you're in the project root and your virtual environment is activated. All commands below should be run inside your configured (virtual) test environment.

---

### 1️⃣ **Discover Devices**

Scan your local network and log all discovered devices to the database.  
_The database file will be created automatically if it doesn't exist._

```bash
sudo python3 -m src.core.discover
```

---

### 2️⃣ **Sniff Network Traffic**

Capture live packets on your network interface and store them as events in the database.

```bash
sudo python3 -m src.core.sniffer
```

---

> **Tip:**  
> Both scripts require `sudo` to access low-level network interfaces.

---

---

## 📸 Screenshots / Demo

![Screenshot of Marauder's Map Network Sentinel in action](<./Screenshots/Untitled%20(1)%20(1).png>)
![Screenshot of Marauder's Map Network Sentinel in action](<./Screenshots/Untitled%20(2)%20(1).png>)
![Screenshot of Marauder's Map Network Sentinel in action](<./Screenshots/Untitled%20(3).png>)

> _Example: Device discovery and live packet capture interface._

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contribution & Support

This is a solo project, but feedback and suggestions are always welcome!  
Feel free to open issues or reach out.

---
