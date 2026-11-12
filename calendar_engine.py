
from datetime import datetime
from zoneinfo import ZoneInfo

from lunar_python import Solar

TIMEZONE = ZoneInfo("Asia/Ho_Chi_Minh")


def get_jieqi_info(lunar, method_name):
    """Safely obtain previous or next solar term."""
    try:
        method = getattr(lunar, method_name)
        jieqi = method()

        if jieqi is None:
            return None

        solar = jieqi.getSolar()

        return {
            "name": jieqi.getName(),
            "datetime": solar.toYmdHms()
        }
    except Exception:
        return None


def calculate_calendar(local_datetime=None):

    if local_datetime:
        dt = datetime.fromisoformat(local_datetime)

        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=TIMEZONE)
        else:
            dt = dt.astimezone(TIMEZONE)
    else:
        dt = datetime.now(TIMEZONE)

    solar = Solar.fromYmdHms(
        dt.year,
        dt.month,
        dt.day,
        dt.hour,
        dt.minute,
        dt.second
    )

    lunar = solar.getLunar()
    eight_char = lunar.getEightChar()

    result = {
        "timezone": "Asia/Ho_Chi_Minh",
        "solar_datetime": dt.strftime("%Y-%m-%d %H:%M:%S"),
        "lunar_date": lunar.toString(),

        "ganzhi": {
            "year": eight_char.getYear(),
            "month": eight_char.getMonth(),
            "day": eight_char.getDay(),
            "hour": eight_char.getTime()
        },

        "previous_jieqi": get_jieqi_info(
            lunar, "getPrevJieQi"
        ),

        "next_jieqi": get_jieqi_info(
            lunar, "getNextJieQi"
        ),

        "status": "CALENDAR_DATA_ONLY",
        "message": (
            "Da tinh can chi va thong tin tiet khi. "
            "Chua tinh am don, duong don va cuc so Ky Mon."
        )
    }

    return result


if __name__ == "__main__":
    import json

    print(json.dumps(
        calculate_calendar(),
        ensure_ascii=False,
        indent=2
    ))
