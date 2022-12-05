"""
Задайте список целых чисел. Найдите сумму элементов списка, имеющих нечетные индексы.

Ввод: значение типа <list> (либо значение типа <int> – размерность списка)
Вывод: значение типа <int>

Примеры:
[2, 3, 5, 9, 3]
12

[5, 1, 5, 2, 7, 11]
14
"""
import random
n = int(input("Введите число N "))
my_list = [random.randint(0, n) for i in range(n)]
print(my_list)

summa = 0
for i in range(1, n, 2):
        summa += my_list[i]
print(summa)