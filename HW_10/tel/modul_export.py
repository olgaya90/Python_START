def write_in_txt(data):
    with open('file.txt', 'a', encoding="utf-8") as file:
        for i in data:
            # print('; '.join(s for s in i), file=file)
            file.write('; '.join(str(s) for s in i) + '\n')


def write_in_csv(data):
    with open('file.csv', 'a', encoding="utf-8") as file:
        for i in data:
            # print('; '.join(s for s in i), file=file)
            file.write('; '.join(str(s) for s in i) + '\n')


def print_from_txt():
    with open('file.txt', 'r', encoding="utf-8") as file:
        for i in file:
            print(i, end="")