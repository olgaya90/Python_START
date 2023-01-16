import modul_search as ms


def get_number():
    print("Для выхода введите в поле Фамилия: exit или 0")
    phones = []
    while (True):
        family = input("Фамилия = ")
        if family == "exit" or family == "0":
            break
        name = input("Имя = ")
        phone = input("Телефон = ")
        note = input("Описание = ")
        input_data = family, name, phone, note
        phones_data = '; '.join(input_data)
        if ms.search_for_similar_in_txt(f'{phones_data}\n'):
            print('Такой контакт уже есть в телефонной книге')
        elif input_data in phones:    # проверка на повторный ввод контакта в одном блоке ввода
            print('Такой контакт уже есть в телефонной книге')
        else:
            phones.append((family, name, phone, note))
    return phones


def get_number_line():
    print("пример: Иванов; Иван; 89172858585; сотовый")
    phones = []
    while (True):
        phones_data = input()
        if phones_data == "exit" or phones_data == "0" or phones_data.count(";") != 3:
            break
        family, name, phone, note = phones_data.split('; ')
        input_data = family, name, phone, note
        if ms.search_for_similar_in_txt(f'{phones_data}\n'):
            print('Такой контакт уже есть в телефонной книге')
        elif input_data in phones:    # проверка на повторный ввод контакта в одном блоке ввода
            print('Такой контакт уже есть в телефонной книге')
        else:
            phones.append((family, name, phone, note))
    return phones
