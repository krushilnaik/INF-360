# INF360 - Programming in Python
# Krushil Naik
# Midterm

from http.server import BaseHTTPRequestHandler, HTTPServer
import re

PORT = 3000
ALPHABET = {}


def fetchAlphabet():
    global ALPHABET

    with open("./alphabet.txt", encoding="utf-8") as alphabetFile:
        CURRENT_CHAR = ""

        for i, line in enumerate(alphabetFile, 1):
            if line[0].isdigit():
                CURRENT_CHAR = line.split(" ", 1)[-1].strip()[1:-1]
                ALPHABET[CURRENT_CHAR] = []
                continue

            ALPHABET[CURRENT_CHAR].append(line.strip())


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


if __name__ == "__main__":
    # server = HTTPServer(("localhost", PORT), Server)

    # print(f"Server up and running on http://localhost:{PORT}")

    # try:
    #     server.serve_forever()
    # except KeyboardInterrupt:
    #     pass

    # server.server_close()

    fetchAlphabet()

    print(*ALPHABET[""], sep="\n")
