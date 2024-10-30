from http.server import BaseHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv
import os

load_dotenv()

port = os.getenv('PORT')
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/healthz':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_error(404, 'Not Found')

def run():
    server = HTTPServer(('localhost', int(port)), MyHandler)
    print("Starting server on localhost:"+port)
    server.serve_forever()

if __name__ == '__main__':
    run()

