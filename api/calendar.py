
import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from calendar_engine import calculate_calendar


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            params = parse_qs(urlparse(self.path).query)
            requested_time = params.get("time", [None])[0]

            result = calculate_calendar(requested_time)

            body = json.dumps(
                result,
                ensure_ascii=False
            ).encode("utf-8")

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(body)

        except Exception as error:
            body = json.dumps({
                "status": "ERROR",
                "message": str(error)
            }, ensure_ascii=False).encode("utf-8")

            self.send_response(500)
            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )
            self.end_headers()
            self.wfile.write(body)
