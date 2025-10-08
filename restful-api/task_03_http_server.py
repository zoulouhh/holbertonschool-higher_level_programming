#!/usr/bin/python3
"""
Module: task_03_http_server
Description:
    A simple HTTP server built using Python's http.server module.
    Demonstrates handling different HTTP GET requests and returning
    plain text or JSON responses.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    A custom HTTP request handler to demonstrate handling GET requests
    and serving JSON data.
    """

    def do_GET(self):
        """
        Handles GET requests for different endpoints.
        """
        # Root endpoint
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            message = "Hello, this is a simple API!"
            self.wfile.write(message.encode("utf-8"))

        # /data endpoint
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("utf-8"))

        # /status endpoint
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode("utf-8"))

        # /info endpoint (optional, as in your example)
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # Undefined endpoints
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """
    Runs the HTTP server on the specified port.
    """
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"🚀 Starting server on port {port}...")
    print(f"Visit: http://localhost:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
