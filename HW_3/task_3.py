"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""
import random
n = int(input("Введите число N "))
my_list = [random.randint(0, n) for i in range(n)]
print(my_list)

maximum = 0
minimum = 1
for i in my_list:
    if type(i) == float:
        if i % 1 < minimum:
            minimum = round(i % 1, 2)
        if i % 1 > maximum:
            maximum = round(i % 1, 2)
print(maximum - minimum)