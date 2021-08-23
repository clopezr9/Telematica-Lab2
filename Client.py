import sys
import http.client

if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()
ip_address = str(sys.argv[1])
port = int(sys.argv[2])

conn = http.client.HTTPConnection(ip_address, port)

while True:
    msg = input()
    if len(msg) != 0:
        msg= "<" + ip_address  + ">" + msg
        conn.request("POST", "/", msg.encode())
        #rsp  = conn.getresponse()

    conn.request("POST","/get",ip_address.encode())
    rsp = conn.getresponse()
    d = rsp.read().decode()
    if len(d) != 0:
        print(d)

    if msg == "exit":
        break

conn.close()
