import  socket
from asyncio import timeout

from IPy import IP

target = input(f"[*] Enter a target to scan : ")
# port = int(input("enter a port to check :"))
port=[80,8080,443,5500]
def portScan(target , port ) :

    try:
        sock = socket.socket()
        # sock,timeout(5)
        sock.connect(( target , port ))
        print(f"port {port} is open ")
    except:
        print(f"Port {port} is closed")

for i in port:
    portScan(target,i)
# sock.close()