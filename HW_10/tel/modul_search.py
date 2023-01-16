import json


def search_for(family, ask):
    with open('data_json.txt', encoding='utf-8') as json_file:
        phones_book = json.load(json_file)
    chet = 0
    for tel in phones_book:
        if tel[ask].lower() == family.lower():
            print(f"{tel['family']}; {tel['name']}; {tel['phone']}; {tel['note']};")
            chet += 1
    if chet == 0:
        print("Таких нет")


def search_for_similar_in_txt(record_find):
    with open('file.txt', 'r', encoding="utf-8") as file:
        record = file.readlines()
        for i in record:
            if i == record_find:
                return True