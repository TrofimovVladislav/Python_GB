# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N,
# и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

import math

def segment_length(x_a, y_a, x_b, y_b):
    length = math.sqrt((pow((x_b - x_a), 2) + pow((y_b - y_a), 2)))
    print (f'Длина отрзека: {round((length), 2)}')

segment_length(5, 7, 4, 3)
segment_length(9, -7, 3, -3)

def segment_length(x_a, y_a, x_b, y_b):
    length = ((pow((x_b - x_a), 2) + pow((y_b - y_a), 2))) ** 0.5
    print (f'Длина отрзека: {round((length), 2)}')

segment_length(5, 7, 4, 3)
segment_length(9, -7, 3, -3)