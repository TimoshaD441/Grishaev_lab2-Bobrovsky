import re

def check_str_for_passport(stroka):
    if re.fullmatch(r"\d{4}\s\d{6}", stroka):
        return 1
    return 0