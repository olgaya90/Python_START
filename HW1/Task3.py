# Напишите программу, которая принимает на вход координаты точки (X и Y) и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
x = int(input('Введите координату х: '))
y = int(input('Введите координату у: '))

def print_xy(x, y, z):
    print(f'x = {x}; y = {y} -> {z}')

if x > 0 and y > 0:
    print_xy(x, y, 1)
elif x > 0 and y < 0:
    print_xy(x, y, 4)
elif x < 0 and y > 0:
    print_xy(x, y, 2)
else:
    print_xy(x, y, 3)