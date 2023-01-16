import json
import os


def convert_to_json(data):
    # проверка на существование файла, проверка на пустоту
    if os.path.exists("data_json.txt") and not os.stat("data_json.txt").st_size == 0:
        with open('data_json.txt', 'r', encoding='utf-8') as json_file:
            phones_book = json.load(json_file)
    else:
        phones_book = []
    for i in data:
        phones_keys = ['family', 'name', 'phone', 'note']
        phones_values = [i[0], i[1], i[2], i[3]]
        phones_book.append(dict(zip(phones_keys, phones_values)))
        with open('data_json.txt', 'w', encoding='utf-8') as outfile:
            json.dump(phones_book, outfile, ensure_ascii=False, indent=4)
            