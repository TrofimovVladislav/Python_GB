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


def util(n):
    g = int(input('Сделайте ход: '))
    if 28 < n:
        print(n-g)
        n = n-g
        if n > 28:
            return util(n)
        else:
            print('Ура!!! Вы Выиграли!!!')
    
util(2021)


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
