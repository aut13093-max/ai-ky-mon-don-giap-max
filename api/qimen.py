
import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from calendar_engine import calculate_calendar
from qimen_rules import create_qimen_structure


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            params = parse_qs(urlparse(self.path).query)
            requested_time = params.get("time", [None])[0]

            calendar_data = calculate_calendar(requested_time)

            chart = create_qimen_structure(calendar_data)

            result = {
                "app": "AI KY MON DON GIAP MAX",
                "method": "Thoi Gia Ky Mon",
                "school": "Chuyen Ban",
                "ju_method": "Thao Bo",
                "timezone": "Asia/Ho_Chi_Minh",
                "calendar": calendar_data,
                "qimen_chart": chart,
                "status": "CALENDAR_CONNECTED",
                "notice": (
                    "Du lieu lich phap da ket noi. "
                    "Chua hoan thanh tinh cuc va lap ban Cuu Cung."
                )
            }

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
