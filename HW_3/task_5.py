"""
Задайте целое число N.
Составьте список чисел Фибоначчи размерность 2N + 1 для отрицательной и положительной части (Негафибоначчи).
https://ru.wikipedia.org/wiki/Негафибоначчи

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
8
[-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""
int_num = int(input("Введите целое число: "))
def fib(n): # функция Фибоначи
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


def reverse_fib(n): # функция Негафибоначи
    return (-1) ** (n + 1) * fib(n)


fib_list = []
for i in range(int_num + 1):
    fib_list.append(reverse_fib(i))

fib_list.reverse()
fib_list.pop(-1)

for i in range(int_num + 1):
    fib_list.append(fib(i))
print(fib_list)