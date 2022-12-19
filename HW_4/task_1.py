"""
Выведите список простых множителей натурального числа N.

Ввод: значение типа <int>
Вывод: значение типа <list>

Примеры:
20
[2, 2, 5]

38
[2, 19]
"""
n = int(input("input number: "))

# n = 2310

lst = []
num = n
i = 2

while i * i <= n:
    while num % i == 0:
        num //= i
        lst.append(i)
        
    i += 1

print(f"Cписок простых множителей числа: {set(lst)}")