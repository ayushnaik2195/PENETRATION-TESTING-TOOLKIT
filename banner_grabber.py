import socket

def banner_grabber(target, port):
    try:
        s = socket.socket()
        s.connect((target, port))
        banner = s.recv(1024)
        print(f"\n[+] Banner: {banner.decode().strip()}")
        s.close()
    except:
        print("[-] Could not grab banner")
