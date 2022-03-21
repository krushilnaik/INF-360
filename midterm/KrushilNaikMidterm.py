# INF360 - Programming in Python
# Krushil Naik
# Midterm

from http.server import BaseHTTPRequestHandler, HTTPServer
import re

# import os

PORT = 3000


class Server(BaseHTTPRequestHandler):
    """Custom HTTP Server"""

    def __init__(self, request, client_address, server):
        self.base = "/midterm/"
        self.path = "/"

        super().__init__(request, client_address, server)

    def do_GET(self):
        """GET requests"""

        STATUS_CODE = 200

        validPath = re.compile(r"^/[a-zA-Z_-]*(.html|.css){0,1}$")

        if not validPath.match(self.path):
            STATUS_CODE = 302
            self.path = "404.html"

        if self.path != "/" and "." not in self.path:
            self.path += ".html"

        # GET /
        if self.path == "/":
            self.path = self.base + "index.html"
        else:
            self.path = self.base + self.path

        try:
            doc = open(self.path[1:], encoding="utf-8").read()
        except FileNotFoundError:
            doc = open(self.base + "404.html", encoding="utf-8").read()

        # split_path = os.path.splitext(self.path)
        # request_extension = split_path[1]

        # if request_extension != ".py":
        self.send_response(STATUS_CODE)
        self.end_headers()
        self.wfile.write(bytes(doc, "utf-8"))
        # else:
        #     self.send_error(404, f"{self.path} not found")


if __name__ == "__main__":
    httpd = HTTPServer(("localhost", PORT), Server)

    print(f"Server up and running on port {PORT}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
