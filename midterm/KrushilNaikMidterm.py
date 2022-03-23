# INF360 - Programming in Python
# Krushil Naik
# Midterm

from http.server import BaseHTTPRequestHandler, HTTPServer
import re

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

        # prevent access to anything that isn't an HTML or CSS file
        validPath = re.compile(r"^/[a-zA-Z_-]*(.html|.css){0,1}$")

        if not validPath.match(self.path):
            STATUS_CODE = 302
            self.path = "404.html"

        # if the request URL is extensionless (e.g. /dashboard)
        # try resolving /dashboard.html instead
        if self.path != "/" and "." not in self.path:
            self.path += ".html"

        # GET /
        if self.path == "/":
            self.path = self.base + "index.html"
        else:
            self.path = self.base + self.path

        # if the requested URL doesn't exist, redirect to the 404 page
        try:
            page = open(self.path[1:], encoding="utf-8").read()
        except FileNotFoundError:
            STATUS_CODE = 404
            page = open(self.base + "404.html", encoding="utf-8").read()

        # send the fetched page
        self.send_response(STATUS_CODE)
        self.end_headers()
        self.wfile.write(bytes(page, "utf-8"))


if __name__ == "__main__":
    httpd = HTTPServer(("localhost", PORT), Server)

    print(f"Server up and running on http://localhost:{PORT}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()
