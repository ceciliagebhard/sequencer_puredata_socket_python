import socket
import sys
import time

data = " ".join(sys.argv[1:])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
UDP_IP = "192.168.0.22"
UDP_PORT = 1982



# MESSAGE = b"Sequencer starts here!"
# python3 catpovsinte.py

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
# print("message: %s" % MESSAGE)



pause=.1
data = [329,0,0,0,440,0,493,0,523,239,329,0,0,349, 523, 0, 0, 0]
for i in range(50):
    for d in data:
        sock.sendto(d.to_bytes(4, 'big'), (UDP_IP, UDP_PORT))
        print("sent:   ", d)
        time.sleep(pause)
        

received = sock.recvfrom(1982)
print(received)
