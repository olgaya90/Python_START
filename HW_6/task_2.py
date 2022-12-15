"""
Задайте список случайных чисел. Выведите:
а) список чисел, которые не повторяются в заданном списке,
б) список повторяемых чисел,
в) список без повторений

Ввод: значение типа <list>
Вывод: три объекта типа <list>

Пример:
[1, 2, 3, 5, 1, 5, 3, 10]
[2, 10]
[1, 3, 5]
[1, 2, 5, 3, 10]
"""
import random

def f(x):
    return random.randint(0, 10)

list1 = [f(i) for i in range(0, 10) ]
print(list1)

list2 = [i for i in list1 if list1.count(i) == 1]
print("список чисел, которые не повторяются в заданном списке", list2)

list3 = set([i for i in list1 if list1.count(i) > 1])
print("список повторяемых чисел ", list(list3))

list4 = list2 + list(list3)
print("список без повторений ", list4)