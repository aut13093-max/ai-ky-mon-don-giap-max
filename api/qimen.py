
import json
from datetime import datetime
from zoneinfo import ZoneInfo
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

from calendar_engine import calculate_calendar
from qimen_ju_table import calculate_ju

TIMEZONE = ZoneInfo("Asia/Ho_Chi_Minh")


def calculate_qimen(requested_time=None):

    calendar = calculate_calendar(requested_time)

    day_ganzhi = calendar["ganzhi"]["day"]

    previous = calendar.get("previous_jieqi")
    next_term = calendar.get("next_jieqi")

    if not previous or not next_term:
        raise ValueError("Khong xac dinh duoc tiet khi")

    previous_time = datetime.fromisoformat(
        previous["datetime"]
    ).replace(tzinfo=TIMEZONE)

    next_time = datetime.fromisoformat(
        next_term["datetime"]
    ).replace(tzinfo=TIMEZONE)

    calculation_time = datetime.fromisoformat(
        calendar["solar_datetime"]
    ).replace(tzinfo=TIMEZONE)

    if not (previous_time <= calculation_time < next_time):
        raise ValueError(
            "Thoi diem tiet khi chua duoc xac minh"
        )

    jieqi_name = previous["name"]

    ju_result = calculate_ju(
        jieqi_name,
        day_ganzhi
    )

    return {
        "app": "AI KY MON DON GIAP MAX",
        "timezone": "Asia/Ho_Chi_Minh",
        "method": "Thoi Gia Ky Mon",
        "school": "Chuyen Ban",
        "ju_method": "Thao Bo",
        "calendar": calendar,
        "qimen": ju_result,
        "status": "PRELIMINARY_JU_CALCULATION",
        "notice": (
            "Da tra cuu cuc so theo bang. "
            "Chua hoan thanh lap ban Cuu Cung."
        )
    }


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            params = parse_qs(urlparse(self.path).query)
            requested_time = params.get("time", [None])[0]

            result = calculate_qimen(requested_time)

            body = json.dumps(
                result,
                ensure_ascii=False
            ).encode("utf-8")

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )
            self.send_header(
                "Access-Control-Allow-Origin", "*"
            )
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
