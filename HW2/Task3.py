# Задайте список размерностью N. Каждый элемент списка вычисляется выражением (1 + 1 / n) ** n,
# где n – позиция (не индекс) элемента в списке, причем 1 < n < N.
# Выведите сумму элементов списка. Ответ округлите до сотых.

number = int(input('Введите число: '))
lst = [round((1 + 1 / i) ** i, 2) for i in range(1, number + 1)]
print(round(sum(lst), 2))