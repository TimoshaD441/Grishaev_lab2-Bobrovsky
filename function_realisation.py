import re

def check_str_for_passport(stroka):
   if re.fullmatch(r"\d{4}\s\d{6}", stroka):
      return 1
   return 0
def search_strs_for_passport(stroka):
    passport_strs = []
    for i in range(len(stroka)-10):
        if check_str_for_passport(stroka[i:i+10]):
            passport_strs.append(stroka[i:i+10])
    return passport_strs
