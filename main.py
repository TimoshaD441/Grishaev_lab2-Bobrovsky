import file_work
import function_realisation

if __name__ == '__main__':
    user_choice = input("Выберите, будете ли вы вводить строку сами или загружать файл \n1 - ввод строки \n2 - файл\n")

    if user_choice == "1":
        user_input_line = input("Введите строку, где нужно искать паспортные данные: ")
        function_realisation.show_passport_data(user_input_line)
    elif user_choice == "2":
        user_file = input("Введите путь к файлу: ")
        user_file_line = file_work.read_file(user_file)
        function_realisation.show_passport_data(user_file_line)
    else:
         print("Некорректное действие")

