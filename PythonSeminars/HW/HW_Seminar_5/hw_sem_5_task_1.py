# можно юзать библиотеку re
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

# import random

# def draw():
#     gamer_1 = 'Игрок №1'
#     gamer_2 = 'Игрок №2'
    
#     print('Для оределения очередности входа по очереди нажмите клавишу "ENTER: ')
#     lot1 = input(f'Клавишу "ENTER" нажимает {gamer_1}: ')
#     if lot1 =='':
#         n1 = random.randint(1, 12)
#         print(f'Игроку №1 выпало число: {n1}')
#         # return n1
#     lot2 = input(f'Клавишу "ENTER" нажимает {gamer_2}: ')
#     if lot2 == '':
#         n2 = random.randint(1, 12)
#         print(f'Игроку №2 выпало число: {n2}')
#         # return n2
#     if n1 > n2:
#         winner_draw = gamer_1
#         print(f'Число {n1} больше {n2}. Начинает {winner_draw}.')
#     else:
#         winner_draw = gamer_2
#         print(f'Число {n2} больше {n1}. \nИгру начинает {winner_draw}.')
        
#     return winner_draw
       
# draw()

# import random

# def draw():
#     gamer_man = 'Человек'
#     gamer_bot = 'Бот'
    
#     print('Для определения очередности хода бросаем жребий: ')
#     lot_1 = input(f'Жребий бросает игрок {gamer_man}. Нажмите "ENTER": ')
#     if lot_1 == '':
#         n_1 = random.randint(1, 12)
#         print(f'Игроку {gamer_man} выпало число: {n_1}')
#     print(f'Жребий бросает игрок {gamer_bot}.')
#     n_2 = random.randint(1, 12)
#     # print(f'Ход {gamer_bot}:')
#     print(f'Игроку {gamer_bot} выпало число: {n_2}')
#     if n_1 > n_2:
#         winner_draw = gamer_man
#         print(f'Число {n_1} больше {n_2}. \nИгру начинает игрок {winner_draw}.')
#     else:
#         winner_draw = gamer_bot
#         print(f'Число {n_2} больше {n_1}. \nИгру начинает игрок {winner_draw}.')
               
#     return winner_draw
       
# draw()

def digi():
    gi = int(input('Введите число на хрен: '))
    return gi

def schet(n):
    n = n - digi()
    print(n)
    if n > 28:
        return schet(n)
    else:
        print('Все')
schet(2021)

# gamer_1 = draw()

# def util(n):
#     if gamer_1 == 'Человек':
#         gamer_2 = 'Бот'
#     else:
#         gamer_2 == 'Человек'
#     if count == 0:
#         print(f'Ход игрока {gamer_2}')
        
#     print(f'Ход игрока {gamer_1}')
#     g = digi()
#     n = n - g
#     print(n)
#     if n > 28:
#         count = 1
#         return util(n)
    
#     else:
#         print('Все')
    # else:
    #     gamer_2 = 'Бот'
    #     print(f'Ход игрока {gamer_2}')
    #     g = digi()
    #     n = n - g
    #     print(f'Остаток после хода Бот{n}')
    #     return util(n)
      
    # # else:
    # #     gamer_2 = 'Бот'
    #     # g = input(f'Ход игрока {gamer_2}. Введите число от 1 до 28: ')
    # print(f'Ход игрока {gamer_2}')
    # g = input(digi())
    # if  not g.isdigit():
    #     print(f'Ошибка ввода. Повторите ввод.')
    #     return digi()
    # # g = int(g)
    # if int(g) > 28:
    #     print(f'Ошибка ввода. Введите число от 1 до 28.')
    #     return digi()
    # else:
    #     g = int(g)
    #     if n > 28:
    #         print(n-g)
    #         n = n-g
    #     if n > 28:
    #         return util(n)
    #     else:
    #         print(f'Осталось {n} конфет.')
    #         print('Ура!!! Вы Выиграли!!! Все конфеты Ваши!!!')
    #         print('Игра окончена :)')
    
# util(2021)



# def util(n):
#     g = input('Сделайте ход: ')
#     if  not g.isdigit():
#         print(f'Введите число от 1 до 28. Введите число заново.')
#         return util(n)
#         g = int(g)
#     # if g > 28:
#     #     print(f'Введите число от 1 до 28. Введите число заново.')
#     #     return util(n)
#     else:
#         g=int(g)
#         if n > 28:
#             print(n-g)
#             n = n-g
#         if n > 28:
#             return util(n)
#         else:
#             print(f'Осталось {n} конфет.')
#             print('Ура!!! Вы Выиграли!!! Все конфеты Ваши!!!')
#             print('Игра окончена :)')
    
# util(2021)


# def util(n):
#     g = input('Сделайте ход: ')
#     if  not g.isdigit():
#         print(f'Введите число от 1 до 28. Введите число заново.')
#         return util(n)
#         g = int(g)
#     # if g > 28:
#     #     print(f'Введите число от 1 до 28. Введите число заново.')
#     #     return util(n)
#     else:
#         g=int(g)
#         if n > 28:
#             print(n-g)
#             n = n-g
#         if n > 28:
#             return util(n)
#         else:
#             print(f'Осталось {n} конфет.')
#             print('Ура!!! Вы Выиграли!!! Все конфеты Ваши!!!')
#             print('Игра окончена :)')
    
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
