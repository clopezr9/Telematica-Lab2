import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

if len(sys.argv) != 3:
	print ("Correct usage: script, IP address, port number")
	exit()

ip_address = str(sys.argv[1])
port = int(sys.argv[2])

messages= {}

class ChatRequestHandler(BaseHTTPRequestHandler):
   
    def do_GET(self):  
        self.send_response(200)
        self.send_header('Content-type','text-html')
        self.end_headers()

        self.wfile.write("OK".encode())

    def do_POST(self):

        if self.path.endswith("/get"):
            content_len = int(self.headers.get('Content-Length'))
            msg = self.rfile.read(content_len).decode()
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            message = messages.get(msg)
            messages[msg] = ""
            self.wfile.write(message.encode())


def main():
    server = HTTPServer((ip_address, port),  ChatRequestHandler)
    print("Server running... :)")
    server.serve_forever()
    
if __name__ == '__main__':
    main()