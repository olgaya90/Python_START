# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве

from math import sqrt

xA = int(input('Введите координату х точки А: '))
yA = int(input('Введите координату у точки А: '))
xB = int(input('Введите координату х точки B: '))
yB = int(input('Введите координату у точки B: '))
print(round(sqrt((xA - xB) ** 2 + (yA - yB) ** 2), 2))