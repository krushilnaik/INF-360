# INF360 - Programming in Python
# Krushil Naik
# Midterm Project

"""
This is a simple website using the current directory as a server.
The frontend (at http://localhost:3000/ after execution) is pretty simple;
Enter some text in the input and hit sumbit for an ASCII art representation.
If your input has an unsupported character, it'll ask you to try something else.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import re, json
import urllib.parse

ALPHABET = {}


def fetchAlphabet():
    """
    Go through alphabet.txt (in this directory)
    and populate the dictionary up top
    to be used as a database for the site
    """

    global ALPHABET

    with open("./alphabet.txt", encoding="utf-8") as alphabetFile:
        CURRENT_CHAR = ""

        for line in alphabetFile:
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

        # API requests
        if self.path.startswith("/api"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            # get the value from the API call and
            # decode it (e.g. %20 turns into a space)
            string = self.path.split("?", 1)[-1][6:]
            string = urllib.parse.unquote(string)

            # Retrieve the ASCII art for each character
            characters = [ALPHABET[_c] for _c in string]

            # Stitch the ASCII letters together into the rows to be displayed on the site
            lines = ["".join(line) for line in zip(*characters)]

            # Send the data back to the site as a JSON object
            self.wfile.write(bytes(json.dumps({"message": lines}), encoding="utf-8"))

            # No need to execute the rest of the code
            return

        validPath = re.compile(r"^/[a-zA-Z_-]*(.html|.css){0,1}$")

        # prevent access to anything that isn't an HTML or CSS file
        # this doesn't let the favicon.ico through
        # but that's okay because there isn't one
        if not validPath.match(self.path):
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
    fetchAlphabet()

    PORT = 3000
    DOMAIN = ("localhost", PORT)

    server = HTTPServer(DOMAIN, Server)

    print(f"Server up and running on http://localhost:{PORT}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    server.server_close()
