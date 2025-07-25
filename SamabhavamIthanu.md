### Abstract: The Marauder's Map: Network Reconnaissance & Anomaly Detector

Inspired by the magical Marauder's Map, which reveals every person's location and movement within Hogwarts, this project proposes an **AI-driven (or rule-based) Network Reconnaissance and Anomaly Detection System**. In the digital realm of "Hogwarts," unauthorized "footprints" (network traffic) and "unregistered animagi" (unauthorized devices) pose significant security risks. This system will continuously monitor network activity, identify connected devices, visualize network topology, and employ detection mechanisms to flag unusual or suspicious behaviors. By providing a clear, real-time "map" of network inhabitants and their activities, this system aims to enhance network visibility, aid in threat detection, and serve as a crucial defense against digital "Dark Arts" without relying on real-time physical simulation or IoT integration.

---

### Key Features of The Marauder's Map Project:

1.  **Network Device Discovery ("Who is here?"):**
    * [cite_start]Automatically identifies and lists all active devices (hosts or "footprints") currently connected to the monitored local network segment[cite: 6099].
    * Captures essential identifying information such as IP addresses and MAC addresses for each discovered device.

2.  **Network Traffic Monitoring ("What are they doing?"):**
    * Captures and analyzes basic network traffic flowing through the system's network interface.
    * [cite_start]Monitors simple traffic statistics for each device, including total bytes sent/received and most used protocols (e.g., HTTP, HTTPS, DNS, TCP, UDP)[cite: 6099].
    * [cite_start]Provides insights into visited domains for web traffic (HTTP/HTTPS) by analyzing DNS requests and TLS SNI, although full URL paths for encrypted traffic are not typically exposed[cite: 6099].

3.  **Interactive Network Map Visualization ("The Map Itself"):**
    * [cite_start]Creates a dynamic, graphical representation of identified devices and their communication pathways (showing who is talking to whom)[cite: 6099].
    * The map dynamically updates as new devices join or leave the network, or as communication patterns change.
    * Allows for basic interaction, potentially displaying more details (IP, MAC, detected services) when a device is selected.

4.  **Basic Anomaly Detection ("Something's Not Right!"):**
    * [cite_start]Employs simple rules or statistical methods to identify network behaviors that deviate from a learned or expected baseline[cite: 6099].
    * Can flag specific suspicious activities, such as new, unrecognized MAC addresses appearing on the network, or devices exhibiting unusually high bandwidth usage (based on predefined thresholds).
    * Identifies attempts at unauthorized network scans or access to restricted ports/services.

5.  **Alert Generation & Logging ("The Daily Prophet"):**
    * Automatically generates alerts (e.g., console messages, simple notifications) when potential anomalies or suspicious activities are detected.
    * Maintains detailed logs of all discovered devices, network activities, and detected alerts for historical review and potential forensic analysis.

6.  **Intuitive User Interface:**
    * A user-friendly interface (e.g., a web-based dashboard or interactive console output) to display the network map, recent alerts, key network statistics, and allow for basic searching or filtering of displayed data.

7.  **Foundational Cybersecurity & Networking Skills Demonstration:**
    * Showcases practical skills in network programming, data parsing, basic data management, and security monitoring fundamentals.

---
**Adherence to Project Constraints:**

* **Solo Project:** The scope is carefully designed to be achievable by an individual developer within the given timeframe (9-10 months), focusing on core functionalities and leveraging existing libraries.
* **No Simulation:** The project operates on real network traffic captured from your local network. It does not simulate quantum phenomena, cryptographic attacks, or large-scale network environments.
* **No IoT:** The system runs entirely on a standard computer and analyzes network data from typical IT devices (laptops, phones, routers, etc.). It does not interact with, control, or rely on any specialized IoT hardware.
* **4 GB RAM Feasibility:** The core tasks (packet processing, data storage, rule-based detection, web interface) are manageable on systems with 4 GB of RAM, avoiding the heavy memory demands of large AI models.

Brainstormer

Show thinking
Okay, vro! Let's map out a detailed work plan for your solo "Mini-Marauder's Map: Network Reconnaissance & Anomaly Detector" project. This plan breaks down the 9-10 month journey into manageable phases, tasks, and deliverables, keeping your solo status and 4GB RAM laptop in mind.

This is your roadmap to an "adipoli" resume project!

Detailed Work Plan: The Marauder's Map: Network Reconnaissance & Anomaly Detector
Project Goal: To develop a functional, interactive system that monitors a local network, identifies connected devices, visualizes network activity, and flags basic anomalies, serving as a personal network security sentinel.

Timeline: 9-10 Months (from current 7th month to 4th month next year)
Team: Solo Developer
Key Constraints: No simulation (of network/IoT, focus on real local network traffic), No IoT devices, 4GB RAM laptop.

Phase 1: Foundation & Initial Reconnaissance (Months 1-2)
Objective: Set up the development environment, establish core network data capture, and implement basic device discovery.

Month 1: Setup & Basic Discovery

Week 1:

Project Planning & Research: Finalize project scope (this detailed plan). Research Scapy / pyshark basics. Understand ARP protocol for device discovery.

Environment Setup: Install Python 3.x. Set up Git repository (GitHub/GitLab). Create and activate a virtual environment (python -m venv marauders_map_env).

Install Core Libraries: pip install scapy

Week 2:

Virtual Network Setup: Install VirtualBox/VMware Workstation Player. Create a small, isolated virtual network (e.g., 2-3 VMs: one Linux, one Windows, one virtual router/switch if comfortable). Configure them to be on a separate subnet from your host machine. This is your safe "Hogwarts Network" for testing.

Basic Device Discovery Script: Write the Python script to perform ARP scans on your virtual network's IP range.

Week 3:

Refine Discovery: Ensure the script reliably finds all active VMs in your virtual network. Handle potential permissions issues (running with sudo/Administrator).

Initial Output: Display discovered IPs and MACs neatly in the console.

Week 4:

Project Structure: Create basic folders for src/, data/, db/, logs/, frontend/.

Basic Logging: Implement Python's logging module to log script activities (scan start/end, devices found).

Version Control: Regular commits to Git.

Month 2: Data Storage & Initial Packet Sniffing

Week 5-6:

Database Design (SQLite): Design a simple SQLite database schema for devices (IP, MAC, first_seen, last_seen, hostname - optional) and network_events (timestamp, source_ip, dest_ip, protocol, port, bytes).

Database Integration: Implement Python functions to connect to SQLite, create tables, and insert/update device information from your discovery script.

Week 7-8:

Basic Packet Sniffing: Learn Scapy's packet sniffing capabilities (sniff() function).

Initial Parsing: Capture packets and extract basic information (source/destination IP, protocol, port, packet size).

Data Ingestion: Store these parsed packet details into your network_events database table.

Test: Run sniffer for a short period, verify data lands in the DB.

Deliverables (End of Phase 1):

Working Python script for network device discovery.

SQLite database setup with devices and network_events tables.

Script to populate/update DB from device discovery and basic packet sniffing.

Clean Git repository.

Phase 2: Backend & Basic Web Visualization (Months 3-5)
Objective: Set up a web backend, create APIs to serve data, and build a basic web interface to display discovered devices and their general activity.

Month 3: Backend API Development

Week 9-10:

Backend Framework: Install pip install Flask (or FastAPI).

API Endpoints: Create Flask routes to:

GET /devices: Return a list of all discovered devices from your SQLite DB.

GET /traffic_summary: Return aggregated traffic data (e.g., total bytes per device, top protocols).

Database Interaction: Ensure Flask app can query your SQLite database.

Week 11-12:

Frontend Setup: Create templates/ and static/ folders for Flask. Basic index.html, style.css, script.js.

Basic Web Display: Fetch data from your Flask API and display a simple list of devices on the web page.

Month 4: Interactive Network Map (Initial Draft)

Week 13-14:

Visualization Library: Research vis.js or Cytoscape.js. Choose one based on ease of use and documentation for basic graph rendering. Install via CDN or npm (if you set up Node.js for frontend, but CDN is simpler for solo).

Map Data Preparation: Write Python code in your Flask app to transform your devices and network_events data into the nodes and edges format required by your chosen visualization library.

Week 15-16:

Render Basic Map: Get your web page to display a static graph of devices (nodes) and basic connections (edges) between them.

Basic Interactivity: Implement clicking on a node to display its IP/MAC.

Month 5: Enhanced Traffic Visualization & Historical View

Week 17-18:

Traffic on Map: Visually represent traffic volume (e.g., thicker lines for more data exchanged).

Protocol/Domain Display: When clicking a device or connection, show top protocols and visited domains (from your parsed data).

Week 19-20:

Historical View: Add a simple way to view historical device presence (e.g., a list of devices seen over time).

Refine UI: Improve the aesthetics of your web interface (colors, layout).

Deliverables (End of Phase 2):

Functional Flask backend serving device and traffic data via API.

Interactive web-based network map displaying devices and connections.

Basic traffic visualization (e.g., line thickness).

Ability to view basic historical data.

Phase 3: Anomaly Detection & Refinement (Months 6-8)
Objective: Implement core anomaly detection logic and integrate alerts into the UI.

Month 6: Rule-Based Anomaly Detection

Week 21-22:

New Device Detection: Implement logic to compare current discovered devices against a "known devices" list (stored in DB). Flag new, unknown MAC addresses.

Unauthorized Port Scan Detection: Implement rules to detect rapid connection attempts to multiple ports from a single source IP in a short time.

Week 23-24:

High Traffic Alert: Implement a simple threshold-based alert for devices sending/receiving unusually large amounts of data.

Alert Storage: Store detected anomalies in a new alerts table in your SQLite DB (timestamp, type, description, source_ip, dest_ip).

Month 7: Statistical Anomaly Detection (Basic)

Week 25-26:

Baseline Creation: Develop a script to collect "normal" network traffic patterns over a period (e.g., a week of your own network activity) and calculate simple statistics (average traffic per device, common protocols used by each).

Deviation Detection: Implement logic to compare current activity against this learned baseline. Flag deviations using simple statistical methods (e.g., Z-score for traffic volume, frequency deviation for protocol usage).

Week 27-28:

Alert Integration: Display these statistical anomaly alerts in your web UI (e.g., a dedicated "Alerts" section).

Filtering: Allow users to filter alerts by type or time.

Month 8: UI/UX & Alert Management Refinement

Week 29-30:

Alert Prioritization (Basic): Assign simple severity levels to alerts (e.g., "High" for new device, "Medium" for high traffic).

Alert Details: When an alert is clicked, show relevant log snippets or traffic data that triggered it.

Week 31-32:

Overall UI Polish: Refine the look and feel of the entire web application. Ensure responsiveness.

Error Handling: Implement basic error handling and user-friendly messages for any issues.

Deliverables (End of Phase 3):

Functional rule-based and basic statistical anomaly detection.

Alerts displayed in the web UI.

Improved user interface and overall system flow.

Phase 4: Finalization, Testing & Documentation (Months 9-10)
Objective: Conduct comprehensive testing, optimize performance, and prepare all final project deliverables.

Month 9: Comprehensive Testing & Optimization

Week 33-36:

Unit Testing: (If time permits, for critical functions).

Integration Testing: Ensure all modules work seamlessly together.

Scenario Testing: Test with various "normal" and "anomalous" scenarios in your virtual network (e.g., connect a new device, run a simple port scan, generate large file transfers).

Performance Tuning: Identify and address any performance bottlenecks (e.g., slow data processing, UI lag). Optimize database queries, data structures.

Refine Anomaly Detection: Reduce false positives/negatives based on testing.

Month 10: Documentation & Presentation

Week 37-38:

Project Report/Thesis: Write the final comprehensive project report, detailing your problem statement, methodology, implementation, results, challenges, and future work.

Code Documentation: Ensure your code is well-commented.

Week 39-40:

Presentation Preparation: Create slides for your project presentation.

Demo Script: Prepare a clear, concise script for demonstrating your "Marauder's Map" features. Practice the demo thoroughly.

Final Review: Review all deliverables for completeness and quality.

Final Deliverables:

Complete, functional "Marauder's Map" application.

Comprehensive Project Report/Thesis.

Well-commented codebase.

Project Presentation.

Demo video (optional, but highly recommended for resume).

Solo Project Success Tips:

Stay Focused: Avoid feature creep. Stick to the plan.

Breaks are Crucial: Don't burn out. Step away when stuck.

Leverage Online Resources: Stack Overflow, official documentation, tutorials are your best friends.

Ask Specific Questions: When you hit a roadblock, formulate very specific questions for online forums or mentors.

Celebrate Small Wins: Each working module is a victory!

This is a challenging but incredibly rewarding journey, vro. You're building a truly "adipoli" project! Let's make it happen!