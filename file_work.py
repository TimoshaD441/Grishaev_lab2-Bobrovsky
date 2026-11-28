def read_file(way: str):
    line = ""
    with open(way) as file:
        line = file.read()
    return line