# INF360 - Programming in Python
# Krushil Naik
# Midterm

from http.server import BaseHTTPRequestHandler, HTTPServer
import re

PORT = 3000


class Server(BaseHTTPRequestHandler):
    """Custom HTTP Server"""

    def do_GET(self):
        """GET requests"""

        STATUS_CODE = 200

        # prevent access to anything that isn't an HTML or CSS file
        validPath = re.compile(r"^/[a-zA-Z_-]*(.html|.css){0,1}$")

        if not validPath.match(self.path):
            print(f"You don't have access to {self.path}.")
            STATUS_CODE = 302
            self.path = "./404.html"
        else:
            self.path = "." + self.path

        # if the request URL is extensionless (e.g. /dashboard)
        # try resolving /dashboard.html instead
        if self.path != "./" and "." not in self.path[1:]:
            self.path += ".html"

        # GET /
        if self.path == "./":
            self.path += "index.html"

        # if the requested URL doesn't exist, redirect to the 404 page
        try:
            page = open(self.path, encoding="utf-8").read()
        except FileNotFoundError:
            STATUS_CODE = 404
            page = open("./404.html", encoding="utf-8").read()

        # send the fetched page
        self.send_response(STATUS_CODE)
        self.end_headers()
        self.wfile.write(bytes(page, "utf-8"))


def fetchAlphabet():
    with open("./alphabet.txt", encoding="utf-8") as alphabetFile:
        for i, line in enumerate(alphabetFile, 1):
            print(i)

            if i > 7:
                return


if __name__ == "__main__":
    httpd = HTTPServer(("localhost", PORT), Server)

    print(f"Server up and running on http://localhost:{PORT}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

    httpd.server_close()

    print(fetchAlphabet())
