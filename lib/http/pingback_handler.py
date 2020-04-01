#!/usr/bin/python
from http.server import BaseHTTPRequestHandler
import json


# This class will handles any incoming request from
# the browser
class PingbackHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # Send the json message
        self.wfile.write(self.get_response())
        return

    def get_response(self):
        pingback_response = {
            "timestamp": 12837323,
            "client": "TrentonZW",
            "server_name": "Mothership"
        }
        string_data = json.dumps(pingback_response)

        return bytes(string_data, 'utf-8')
