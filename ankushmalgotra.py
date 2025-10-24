from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import urllib.parse

PORT = 8081  # Browser will open on localhost:8081

number_to_guess = random.randint(1, 10)

class GuessHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        message = ""

        if "guess" in params:
            try:
                guess = int(params["guess"][0])
                if guess < number_to_guess:
                    message = "Too low!"
                elif guess > number_to_guess:
                    message = "Too high!"
                else:
                    message = "Correct! 🎉"
            except ValueError:
                message = "Enter a valid number!"

        # HTML page
        html = f"""
        <html>
        <head><title>Number Guessing Game</title></head>
        <body>
            <h1>Welcome to Ankush's Number Guessing Game!</h1>
            <p>Guess a number between 1 and 10:</p>
            <form method="get">
                <input type="text" name="guess" />
                <input type="submit" value="Submit" />
            </form>
            <p>{message}</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

# Run the server
server = HTTPServer(("0.0.0.0", PORT), GuessHandler)
print(f"Server running on http://localhost:{PORT}")
server.serve_forever()
