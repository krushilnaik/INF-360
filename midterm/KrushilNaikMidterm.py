# INF360 - Programming in Python
# Krushil Naik
# Midterm Project

"""
This is a simple website using the current directory as a server.
The frontend (http://localhost:3000) is pretty simple;
Enter some text and hit sumbit for an ASCII art representation.
If you typed an unsupported character, it'll alert you.

I wrote as much of the functionality in this Python file as possible,
but the DOM manipulation logic needed to be in JavaScript (found in index.html).
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import re, json
import urllib.parse

ALPHABET = {}


def openFile(path: str):
    """
    We're only ever using UTF-8 files in this project,
    so set it in here and just use this everywhere.

    Args:
        path (str): the file path to open

    """
    return open(path, encoding="utf-8")


def fetchAlphabet():
    """
    Go through `alphabet.txt` (in this directory)
    and populate the dictionary up top
    to be used as a database for the site
    """

    global ALPHABET

    with openFile("./alphabet.txt") as alphabetFile:
        letter = ""

        for line in alphabetFile:
            if line[0].isdigit():
                # gets the second half of the line, without the quotes
                # e.g. 33 '!' -> !
                letter = line.split(" ", 1)[-1].strip()[1:-1]

                # Add the fetched character to the database
                # mapped to list populated in future iterations
                ALPHABET[letter] = []
                continue

            ALPHABET[letter].append(line.strip())


class MyServer(BaseHTTPRequestHandler):
    """
    Custom HTTP Server

    GET / -> index.html

    GET /api?value=<value> -> build ASCII art for <value> and respond with JSON

    GET /<anything-else> -> <anything-else>.html if it exists, else 404.html
    """

    def __init__(self, request, client_address, server):
        # Wannabe middleware that doesn't let anything but HTML and CSS through
        self.validPaths = re.compile(r"^/[a-zA-Z_-]*(.html|.css){0,1}$")

        super().__init__(request, client_address, server)

    def do_GET(self):
        """GET requests"""

        STATUS_CODE = 200

        # API requests
        # e.g. http://localhost:3000/api?value=hello%20world
        if self.path.startswith("/api?value="):

            # let the browser know it's getting some JSON data back
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            # get the value from the API call and
            # decode it (e.g. `hello%20world` -> `hello world`)
            string = self.path.split("?", 1)[-1][6:]
            string = urllib.parse.unquote(string)

            c = string[0]

            # Retrieve the ASCII art for each character
            # If the character isn't supported, ask the user to try again
            try:
                characters = [ALPHABET[(c := _c)] for _c in string]
            except KeyError:
                self.wfile.write(
                    bytes(
                        json.dumps({"unsupported": c}),
                        encoding="utf-8",
                    )
                )
                return

            # Stitch the ASCII letters together into the rows to be displayed on the site
            lines = ["".join(line) for line in zip(*characters)]

            # Send the data back to the site as a JSON object
            # Response format (for /api?value=hello%20world):
            #
            # {
            #     "message": [
            #         "#...........#.....#...................................#.........#.",
            #         "#......###..#.....#......###........#...#..###...###..#.........#.",
            #         "####..#...#.#.....#.....#...#.......#.#.#.#...#.#.....#......####.",
            #         "#...#.####..#.....#.....#...#.......#.#.#.#...#.#.....#.....#...#.",
            #         "#...#.#.....#.....#.....#...#.......#.#.#.#...#.#.....#.....#...#.",
            #         "#...#..####..##....##....###.........#.#...###..#......##....####.",
            #         ".................................................................."
            #     ]
            # }
            #
            self.wfile.write(bytes(json.dumps(lines), encoding="utf-8"))

            # No need to execute the rest of the code
            return

        # prevent access to non-HTML/CSS files
        # this doesn't let favicon.ico through
        # but that's okay because there isn't one
        if not self.validPaths.match(self.path):
            STATUS_CODE = 302
            self.path = "./404.html"
        else:
            self.path = "." + self.path

        # if request URL is extensionless (e.g. ./dashboard)
        # try resolving /dashboard.html instead
        if self.path != "./" and "." not in self.path[1:]:
            self.path += ".html"

        # GET /
        if self.path == "./":
            self.path += "index.html"

        # Try to open the requested file
        # if it doesn't exist, redirect to the 404 page
        try:
            page = openFile(self.path)
        except FileNotFoundError:
            STATUS_CODE = 404
            page = openFile("./404.html")

        # send the fetched page
        self.send_response(STATUS_CODE)
        self.end_headers()
        self.wfile.write(bytes(page.read(), "utf-8"))

        page.close()


if __name__ == "__main__":
    fetchAlphabet()

    # `DOMAIN` isn't used but I'm keeping it there
    # in case it's useful in the final project
    HOST = (DOMAIN := "localhost", PORT := 3000)

    server = HTTPServer(HOST, MyServer)

    print(f"Server up and running on http://localhost:{PORT}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
