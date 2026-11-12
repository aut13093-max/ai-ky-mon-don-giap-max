
def get_yuan(day_ganzhi):
    """
    Determine Yuan (上元、中元、下元)
    from the day stem-branch.

    This is an interface only.
    Validated Jia-Zi group rules
    must be implemented before use.
    """
    raise NotImplementedError(
        "Yuan calculation rules are not yet validated."
    )


def calculate_dun_and_ju(jieqi, yuan):
    """
    Determine:
    - Yang Dun or Yin Dun
    - Ju number 1-9

    Requires a verified Jieqi-to-Ju table
    for the chosen Chai Bu method.
    """
    raise NotImplementedError(
        "Chai Bu Dun-Ju table is not yet implemented."
    )


def create_qimen_structure(calendar_data):
    """
    Prepare data for the Qimen chart engine.
    Do not generate a chart until the
    Dun-Ju calculation is verified.
    """
    return {
        "calendar": calendar_data,
        "dun_type": None,
        "ju_number": None,
        "yuan": None,
        "status": "RULES_NOT_VALIDATED",
        "message": (
            "Chua xac minh quy tac Thao Bo. "
            "Khong tao ban menh gia."
        )
    }
