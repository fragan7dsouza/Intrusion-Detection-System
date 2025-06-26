import socket

target_ip = "192.168.1.104"  #local IP

for port in range(20, 60):  # expanded rangefor better detect detection
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.2)
        sock.connect((target_ip, port))
        sock.close()
    except:
        pass
