from logger import log
import json


@log
def get_data() -> list:
    """
    Выгружает данные из файла и возвращает словарь
    Если id существует, то возвращает только одну запись по id
    """
    with open("HW_10\db.json", 'r', encoding="utf-8") as file:
        data_file = json.load(file)
    return data_file["items"]
