import socket
from IPy import IP

ports = [80, 8080, 443, 5500,22,23, 53]

def grabBanner(s):
    return s.recv(1024)

def port_scan(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                banner = grabBanner(sock)
                print(f"[+] Port {port} is open and is running {banner}")
            except:
                print(f"[+] Port {port} is open but noting to grab")

        sock.close()

    except:
        pass

def scan(target):
    print(f"\n[*] Scanning target: {target}")
    for port in ports:
        port_scan(target, port)

targets = input("[*] Enter target(s) (comma-separated): ")

if "," in targets:
    for ip in targets.split(","):
        scan(ip.strip())
else:
    scan(targets.strip())