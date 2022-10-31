# можно юзать библиотекe re
# задача 1. Создайте программу для игры с конфетами человек против бота.

# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота

# а) Подумайте как наделить бота ""интеллектом""

# import re

# result = re.match(r'AV', 'AV Analytics Vidhya AV')
# print(result.group(0))

# result = re.match(r'AV', 'AV Analytics Vidhya AV')
# print (result.start())
# print (result.end())

import random

def draw(n):
    lot1 = input(f'Для определения очередности хода нажмите клавишу "ENTER"')
    for i in range(n)
    if lot1 == '':
        n = random.randint(1, 13)
        print(f'У Игрока №1 выпало число: {n}')
        lot2 = input(f'Для определения очередности хода нажмите клавишу "ENTER"')
        n = random.randint(1, 13)
        print(f'У Игрока №2 выпало число: {n}')
      
draw(2)




# print(f'У первого игрока выпала цифра: {lot1}')
# lot2 = input('Выбор Игрока #2: ', (random.randint(1, 6)))
# print(f'У второго игрока выпала цифра: {lot2}')
    
    

# def draw(x, y):
#     if lot1 > lot2:
#         print('Начинает первый игрок')
#     else:
#         print('Начинает второй игрок')

# draw(lot1, lot2)


# exit()
# def util(n):
#     g = int(input('Сделайте ход: '))
#     if 28 < n:
#         print(n-g)
#         n = n-g
#         if n > 28:
#             return util(n)
#         else:
#             print('Ура!!! Вы Выиграли!!!')
    
# util(2021)


# def util(n):
#     g = int(input('Сделайте ход: '))
#     if  0 < n <= 28: 
#         print('Ура')
#     else:
#         if  28 < n <= 0:
#             print(n-g)
#             n = n-g
#             return util(n)
    
# util(2021)



    
# def check_int():
#     """
#     Функция проверяет является ли введенное значение числом.
#     """
#     input_data = input('Введите номер дня недели: ')
#     if not input_data.isdigit():
#         print(f'Вы ввели не число.\nПовторите ввод. ')
#         return check_int()
#     else:
#         return input_data
