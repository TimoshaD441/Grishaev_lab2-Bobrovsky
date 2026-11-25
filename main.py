import function_realisation

if __name__ == '__main__':
    stroka = str(input())
    dannie = function_realisation.search_strs_for_passport(stroka)
    for i in range(len(dannie)):
        print(dannie[i])
