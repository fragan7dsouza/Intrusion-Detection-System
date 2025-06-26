# ids_engine.py

from scapy.all import sniff, IP, TCP
import logging
import threading
import queue

logging.basicConfig(
    filename="suspicious_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

ip_activity = {}
alert_queue = None
sniffing_thread = None
stop_event = threading.Event()

def detect_packet(packet):
    if stop_event.is_set():
        return

    if packet.haslayer(IP) and packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport

        print(f"packet from {src_ip}:{dst_port}")

        if src_ip not in ip_activity:
            ip_activity[src_ip] = []

        ip_activity[src_ip].append(dst_port)

        if len(set(ip_activity[src_ip])) > 5:
            alert = f"[alert] port scan detected from {src_ip}"
            print(alert)
            logging.info(alert)
            if alert_queue:
                alert_queue.put(alert)

def sniff_packets():
    sniff(filter="tcp", prn=detect_packet, store=0, stop_filter=lambda x: stop_event.is_set())

def start_sniffing():
    global sniffing_thread
    stop_event.clear()
    sniffing_thread = threading.Thread(target=sniff_packets, daemon=True)
    sniffing_thread.start()

def stop_sniffing():
    stop_event.set()

def get_alerts():
    alerts = []
    while not alert_queue.empty():
        try:
            alerts.append(alert_queue.get_nowait())
        except queue.Empty:
            break
    return alerts
