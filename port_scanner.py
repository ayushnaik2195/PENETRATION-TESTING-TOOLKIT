import socket

def port_scanner(target):
    print(f"\nScanning {target}...\n")
    for port in range(1, 1025):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect((target, port))
            print(f"[+] Port {port} is OPEN")
            s.close()
        except:
            pass
