# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

a = int(input('Введите цифру от 1 до 7: '))
if 1 <= a <= 5:
    print('false')
elif 6 <= a <= 7:
    print('true')
else:
    print('Введите число от 1 до 7!')