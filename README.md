# 🛡️ Intrusion Detection System (IDS)

A lightweight Python-based Intrusion Detection System that monitors real-time TCP traffic to detect potential port scanning attacks. Built using **Scapy** for packet sniffing and **Tkinter** for an interactive GUI.

---

## ⚙️ Features

- ✅ Real-time packet sniffing using Scapy  
- ✅ Detection of suspicious IPs scanning multiple TCP ports  
- ✅ GUI built with Tkinter  
- ✅ Start/Stop monitoring controls  
- ✅ Live alert feed  
- ✅ View logs from previous sessions  
- ✅ Light/Dark mode toggle

---

## 🖥️ GUI Preview

<img src="https://via.placeholder.com/600x300?text=IDS+GUI+Preview" alt="GUI Screenshot" width="600"/>

---

## 📁 Project Structure

```
Intrusion-Detection-System/
│
├── gui.py               # main user interface
├── ids_engine.py        # packet sniffing and detection logic
├── simulate_tcp.py      # test script to simulate a port scan
├── suspicious_log.txt   # log file for suspicious activity
├── README.md            # project documentation
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.x installed  
- Install dependencies using pip:

```bash
pip install scapy
```

---

### 🖱️ How to Run

1. **Launch the GUI:**

```bash
python gui.py
```

2. **Start Monitoring** from the GUI.

3. In another terminal, simulate a TCP port scan:

```bash
python simulate_tcp.py
```

4. Detected intrusions will appear in the GUI and log file.

---

## 🧪 simulate_tcp.py

This file simulates a port scan by attempting rapid TCP connections across a range of ports on your local machine.

Make sure the `target_ip` matches your system's local IP (`ipconfig` on Windows to check).

---

## 📄 Log File

Suspicious activity is saved in `suspicious_log.txt` with timestamps for future reference.

---

## 📌 Notes

- Designed for educational and testing purposes only.  
- Windows users may need to run the terminal/VS Code as **Administrator** to allow packet sniffing.

---

## 👨‍💻 Author

**Fragan Dsouza**  
📎 [LinkedIn](www.linkedin.com/in/fragan-d-souza-64626a29b)  
💻 [GitHub](https://github.com/fragan7dsouza)

---

## 📜 License

This project is open-source and free to use under the MIT License.
