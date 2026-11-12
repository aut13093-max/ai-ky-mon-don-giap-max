
# AI KY MON DON GIAP MAX
# Thoi Gia Ky Mon - Chai Bu Ju Table
# Version 1.0 - Calculation module

# IMPORTANT:
# This module calculates the traditional Ju table lookup.
# Full Chai Bu boundary handling and chart arrangement
# still require independent verification.

JU_TABLE = {
    "冬至": ("阳遁", 1, 7, 4),
    "小寒": ("阳遁", 2, 8, 5),
    "大寒": ("阳遁", 3, 9, 6),
    "立春": ("阳遁", 8, 5, 2),
    "雨水": ("阳遁", 9, 6, 3),
    "惊蛰": ("阳遁", 1, 7, 4),
    "春分": ("阳遁", 3, 9, 6),
    "清明": ("阳遁", 4, 1, 7),
    "谷雨": ("阳遁", 5, 2, 8),
    "立夏": ("阳遁", 4, 1, 7),
    "小满": ("阳遁", 5, 2, 8),
    "芒种": ("阳遁", 6, 3, 9),

    "夏至": ("阴遁", 9, 3, 6),
    "小暑": ("阴遁", 8, 2, 5),
    "大暑": ("阴遁", 7, 1, 4),
    "立秋": ("阴遁", 2, 5, 8),
    "处暑": ("阴遁", 1, 4, 7),
    "白露": ("阴遁", 9, 3, 6),
    "秋分": ("阴遁", 7, 1, 4),
    "寒露": ("阴遁", 6, 9, 3),
    "霜降": ("阴遁", 5, 8, 2),
    "立冬": ("阴遁", 6, 9, 3),
    "小雪": ("阴遁", 5, 8, 2),
    "大雪": ("阴遁", 4, 7, 1),
}

# Three Yuan classification by Fu Tou branch
UPPER = {"子", "午", "卯", "酉"}
MIDDLE = {"寅", "申", "巳", "亥"}
LOWER = {"辰", "戌", "丑", "未"}

# Complete 60 Jia-Zi cycle
GANZHI_CYCLE = [
    "甲子", "乙丑", "丙寅", "丁卯", "戊辰",
    "己巳", "庚午", "辛未", "壬申", "癸酉",

    "甲戌", "乙亥", "丙子", "丁丑", "戊寅",
    "己卯", "庚辰", "辛巳", "壬午", "癸未",

    "甲申", "乙酉", "丙戌", "丁亥", "戊子",
    "己丑", "庚寅", "辛卯", "壬辰", "癸巳",

    "甲午", "乙未", "丙申", "丁酉", "戊戌",
    "己亥", "庚子", "辛丑", "壬寅", "癸卯",

    "甲辰", "乙巳", "丙午", "丁未", "戊申",
    "己酉", "庚戌", "辛亥", "壬子", "癸丑",

    "甲寅", "乙卯", "丙辰", "丁巳", "戊午",
    "己未", "庚申", "辛酉", "壬戌", "癸亥"
]


def get_yuan_from_futou(day_ganzhi):
    """
    Determine Yuan from Jia/Ji Fu Tou.

    Input examples:
        甲子 -> 上元
        甲戌 -> 下元
        己巳 -> 中元
    """

    if not isinstance(day_ganzhi, str):
        raise ValueError("日干支必须是字符串")

    if len(day_ganzhi) != 2:
        raise ValueError("日干支格式错误")

    stem = day_ganzhi[0]
    branch = day_ganzhi[1]

    if stem not in {"甲", "己"}:
        raise ValueError("符头必须是甲日或己日")

    if branch in UPPER:
        return "上元"

    if branch in MIDDLE:
        return "中元"

    if branch in LOWER:
        return "下元"

    raise ValueError("无法识别符头地支")


def find_futou(day_ganzhi):
    """
    Find the nearest Jia or Ji day on or before
    the given day in the 60 Jia-Zi cycle.
    """

    if day_ganzhi not in GANZHI_CYCLE:
        raise ValueError("无效的日干支")

    current_index = GANZHI_CYCLE.index(day_ganzhi)

    for offset in range(60):
        candidate = GANZHI_CYCLE[
            (current_index - offset) % 60
        ]

        if candidate.startswith(("甲", "己")):
            return {
                "futou": candidate,
                "days_before": offset,
                "yuan": get_yuan_from_futou(candidate)
            }

    raise ValueError("无法找到符头")


def get_ju(jieqi_name, yuan):
    """
    Get Dun type and Ju number from solar term
    and Yuan.
    """

    if jieqi_name not in JU_TABLE:
        raise ValueError(
            f"未知节气: {jieqi_name}"
        )

    if yuan not in {"上元", "中元", "下元"}:
        raise ValueError("无效三元")

    dun_type, upper, middle, lower = JU_TABLE[jieqi_name]

    ju_map = {
        "上元": upper,
        "中元": middle,
        "下元": lower
    }

    return {
        "jieqi": jieqi_name,
        "dun_type": dun_type,
        "yuan": yuan,
        "ju_number": ju_map[yuan],
        "status": "JU_TABLE_LOOKUP_ONLY"
    }


def calculate_ju(jieqi_name, day_ganzhi):
    """
    Combined calculation:
    1. Find Fu Tou.
    2. Determine Yuan.
    3. Look up Dun type and Ju number.

    Important:
    This does not independently determine which
    solar term is active at the exact calculation time.
    """

    futou_data = find_futou(day_ganzhi)

    ju_data = get_ju(
        jieqi_name,
        futou_data["yuan"]
    )

    return {
        "day_ganzhi": day_ganzhi,
        "futou": futou_data["futou"],
        "days_before_futou": futou_data["days_before"],
        "yuan": futou_data["yuan"],
        "dun_type": ju_data["dun_type"],
        "ju_number": ju_data["ju_number"],
        "jieqi": jieqi_name,
        "status": "PRELIMINARY_RULE_LOOKUP",
        "warning": (
            "Chua xac minh day du quy tac Thao Bo "
            "va thoi diem giao tiet."
        )
    }


if __name__ == "__main__":
    import json

    test = calculate_ju("冬至", "乙丑")

    print(json.dumps(
        test,
        ensure_ascii=False,
        indent=2
    ))
