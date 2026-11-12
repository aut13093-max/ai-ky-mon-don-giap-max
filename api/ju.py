
import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from qimen_ju_table import get_yuan_from_futou, get_ju


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            params = parse_qs(urlparse(self.path).query)

            jieqi = params.get("jieqi", [None])[0]
            futou = params.get("futou", [None])[0]

            if not jieqi or not futou:
                raise ValueError(
                    "Can tham so jieqi va futou"
                )

            yuan = get_yuan_from_futou(futou)
            result = get_ju(jieqi, yuan)

            result["jieqi"] = jieqi
            result["futou"] = futou

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

            self.send_response(400)
            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )
            self.end_headers()
            self.wfile.write(body)
