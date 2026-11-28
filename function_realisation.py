import re

def check_str_for_passport(line):
   if re.fullmatch(r"\d{4}\s\d{6}", line):
      return 1
   return 0

def find_passport_data(line):
    passport_strs = []
    for i in range(len(line)-10):
        if check_str_for_passport(line[i:i+11]) == 1:
            passport_strs.append(line[i:i+11])
    return passport_strs

def show_passport_data(line: str):
    data = find_passport_data(line)
    for i in range(len(data)):
        print(data[i])