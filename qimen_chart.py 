
# AI KY MON DON GIAP MAX
# Nine Palace Earth Plate Engine
# Version 1.0

# Luo Shu palace sequence
LUO_SHU = [
    {"number": 1, "name": "Khảm", "direction": "Bắc"},
    {"number": 2, "name": "Khôn", "direction": "Tây Nam"},
    {"number": 3, "name": "Chấn", "direction": "Đông"},
    {"number": 4, "name": "Tốn", "direction": "Đông Nam"},
    {"number": 5, "name": "Trung", "direction": "Trung Tâm"},
    {"number": 6, "name": "Càn", "direction": "Tây Bắc"},
    {"number": 7, "name": "Đoài", "direction": "Tây"},
    {"number": 8, "name": "Cấn", "direction": "Đông Bắc"},
    {"number": 9, "name": "Ly", "direction": "Nam"},
]

# Earth plate stems
EARTH_STEMS = [
    "戊", "己", "庚", "辛", "壬",
    "癸", "丁", "丙", "乙"
]


def create_earth_plate(dun_type, ju_number):

    if dun_type not in ("阳遁", "阴遁"):
        raise ValueError("Invalid Dun type")

    if not isinstance(ju_number, int) or not 1 <= ju_number <= 9:
        raise ValueError("Ju number must be between 1 and 9")

    # Yang Dun moves forward.
    # Yin Dun moves backward.
    palace_order = [p["number"] for p in LUO_SHU]

    start_index = palace_order.index(ju_number)

    if dun_type == "阳遁":
        direction = 1
    else:
        direction = -1

    result = {}

    for i, stem in enumerate(EARTH_STEMS):

        palace_index = (
            start_index + direction * i
        ) % 9

        palace_number = palace_order[palace_index]

        palace = next(
            p for p in LUO_SHU
            if p["number"] == palace_number
        )

        result[str(palace_number)] = {
            "palace": palace["name"],
            "direction": palace["direction"],
            "stem": stem
        }

    return {
        "dun_type": dun_type,
        "ju_number": ju_number,
        "earth_plate": result,
        "status": "EARTH_PLATE_PRELIMINARY"
    }


def create_chart(qimen_data):

    dun_type = qimen_data.get("dun_type")
    ju_number = qimen_data.get("ju_number")

    plate = create_earth_plate(
        dun_type,
        ju_number
    )

    return {
        "method": "Thoi Gia Ky Mon",
        "school": "Chuyen Ban",
        "ju_method": "Thao Bo",
        "earth_plate": plate["earth_plate"],
        "dun_type": dun_type,
        "ju_number": ju_number,
        "status": "EARTH_PLATE_ONLY",
        "notice": (
            "Day la dia ban so bo. "
            "Chua co thien ban, nhan ban, "
            "bat mon, bat than va gia tri tri phu."
        )
    }


if __name__ == "__main__":
    import json

    test = create_earth_plate("阳遁", 1)

    print(json.dumps(
        test,
        ensure_ascii=False,
        indent=2
    ))
