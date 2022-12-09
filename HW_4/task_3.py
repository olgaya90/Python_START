"""
Задать натуральное число k.
Сформируйте многочлен (полином) степени k со случайными коэффициентами из промежутка от 0 до 100, включительно.
Многочлен вывести в консоль и записать в файл.

Ввод: значение типа <int>
Вывод: значение типа <str>, файл с одной строкой.

Пример:
2
2x^2 + 4x + 5 = 0
"""

import random

k = int(input("Input degree k: "))
lst = []

def rnd():
    return random.randint(0, 100)


for i in range(k, 1, -1):
    c = rnd()
    if c:
        lst.append(f'{c}x^{i}')

c = rnd()
if c:
    lst.append(f'{c}x')
c = rnd()
if c:
    lst.append(f'{c}')

res = ' + '.join(lst) + ' = 0'

print(res)