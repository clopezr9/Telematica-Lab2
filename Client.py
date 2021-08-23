import sys
import http.client
import threading
import time
from requests import get

if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()

ip_address = str(sys.argv[1])
port = int(sys.argv[2])

my_ip = get('https://api.ipify.org').text

conn = http.client.HTTPConnection(ip_address, port)

def get_messages():
    while True:
        conn.request("POST", "/get", ip_address.encode())
        rsp = conn.getresponse()
        d = rsp.read().decode()
        if len(d) != 0:
            print(d)
        time.sleep(3)

thread = threading.Thread(target=get_messages, daemon=True)
thread.start()

while True:
    msg = input()

    if len(msg) != 0:
        msg=  my_ip  + "->" + msg
        conn.request("POST", "/", msg.encode())
        rsp  = conn.getresponse()
