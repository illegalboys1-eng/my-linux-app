# Simple Python web server
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from my Docker container!")

    def log_message(self, format, *args):
        pass

print("Server running on port 5000...")
HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
