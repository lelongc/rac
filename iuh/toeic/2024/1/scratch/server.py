import os
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

class QuietHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=r"d:\folder\rac\iuh\toeic\2024\1\web", **kwargs)
    
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def log_message(self, format, *args):
        # Print basic access log for visibility
        print(f"[{self.log_date_time_string()}] {format % args}")

if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = ThreadingHTTPServer(server_address, QuietHandler)
    print("Serving HTTP on 0.0.0.0 port 8080 (http://localhost:8080/) ...")
    httpd.serve_forever()
