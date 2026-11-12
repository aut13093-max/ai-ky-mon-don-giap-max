
# Thoi Gia Ky Mon - Chai Bu Ju Table
# Standard 24 solar-term mapping

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

UPPER = {"子", "午", "卯", "酉"}
MIDDLE = {"寅", "申", "巳", "亥"}
LOWER = {"辰", "戌", "丑", "未"}


def get_yuan_from_futou(day_ganzhi):
    """
    Input: Jia or Ji day ganzhi, e.g. 甲子 / 己酉.
    """
    if not day_ganzhi or len(day_ganzhi) < 2:
        raise ValueError("Invalid day ganzhi")

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


def get_ju(jieqi_name, yuan):
    if jieqi_name not in JU_TABLE:
        raise ValueError("未知节气，不能计算局数")

    dun, upper, middle, lower = JU_TABLE[jieqi_name]

    yuan_map = {
        "上元": upper,
        "中元": middle,
        "下元": lower
    }

    if yuan not in yuan_map:
        raise ValueError("无效三元")

    return {
        "dun_type": dun,
        "yuan": yuan,
        "ju_number": yuan_map[yuan],
        "status": "JU_TABLE_LOOKUP_ONLY"
    }
