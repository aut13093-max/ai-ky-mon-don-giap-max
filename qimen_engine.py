
from datetime import datetime
from zoneinfo import ZoneInfo

TIMEZONE = ZoneInfo("Asia/Ho_Chi_Minh")

STEMS = [
    "Giáp", "Ất", "Bính", "Đinh", "Mậu",
    "Kỷ", "Canh", "Tân", "Nhâm", "Quý"
]

BRANCHES = [
    "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ",
    "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"
]

PALACES = {
    "Tốn": "Đông Nam",
    "Ly": "Chính Nam",
    "Khôn": "Tây Nam",
    "Chấn": "Chính Đông",
    "Trung": "Trung Tâm",
    "Đoài": "Chính Tây",
    "Cấn": "Đông Bắc",
    "Khảm": "Chính Bắc",
    "Càn": "Tây Bắc"
}

def get_local_time():
    return datetime.now(TIMEZONE)

def get_hour_branch(dt):
    hour = dt.hour
    index = ((hour + 1) // 2) % 12
    return BRANCHES[index]

def get_hour_range(dt):
    branch = get_hour_branch(dt)
    return branch

def get_palaces():
    return PALACES

def create_basic_chart():
    now = get_local_time()

    return {
        "timezone": "Asia/Ho_Chi_Minh",
        "local_time": now.strftime("%Y-%m-%d %H:%M:%S"),
        "hour_branch": get_hour_branch(now),
        "palaces": get_palaces(),
        "status": "BASIC_DATA_ONLY",
        "message": (
            "Chưa hoàn thành tính toán tiết khí, "
            "âm dương độn và cục số."
        )
    }

if __name__ == "__main__":
    import json
    print(json.dumps(
        create_basic_chart(),
        ensure_ascii=False,
        indent=2
    ))
