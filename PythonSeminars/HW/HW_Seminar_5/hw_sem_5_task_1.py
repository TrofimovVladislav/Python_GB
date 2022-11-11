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

import random

def draw():
    gamer_man = 'Человек'
    gamer_bot = 'Бот'
       
    print('\nДля определения очередности хода бросаем жребий: \n')
    lot_1 = input(f'Жребий бросает игрок {gamer_man}.\nЧтобы сделать ход нажмите "ENTER": ')
    
    if lot_1 == '':
        n_1 = random.randint(1, 3)
        print(f'Игроку {gamer_man} выпало число: {n_1}\n')

    print(f'Жребий бросает игрок {gamer_bot}.')
    n_2 = random.randint(1, 3)
    print(f'Игроку {gamer_bot} выпало число: {n_2}\n')
    
    if n_1 == n_2:
        print(input('Ничья. Пребросьте жребий.\nДля продолжения нажмите "ENTER": '))
        return draw()
    elif n_1 > n_2:
        winner_draw = gamer_man
        looser_draw = gamer_bot
        print(f'Число {n_1} больше {n_2}. \nИгру начинает игрок {winner_draw}.\n')
    else:
        winner_draw = gamer_bot
        looser_draw = gamer_man
        print(f'Число {n_2} больше {n_1}. \nИгру начинает игрок {winner_draw}.\n')
        print(f'ВИННЕР {winner_draw}')
              
    return winner_draw
    
gamer_win = draw()


def digi():
    gi = input('Введите число на хрен: ')
    if not gi.isdigit():
        print('Неверно. Повторите.')
        return digi()
    elif int(gi) <= 0 or int(gi) > 1000:
        print('Неверно. Повторите.')
        return digi()
    else:
        return int(gi)

def util(n):
    gamer_1 = gamer_win
    count = 0
    gamer2 = ''    
    if gamer_1 == 'Человек':
        gamer_2 = 'Бот'
    else:
        gamer_1 = 'Бот'
        gamer_2 = 'Человек'
    if count == 0:
        print(f'Ход игрока {gamer_1}.')
        g = digi()
        n = n - g
        count == 1
        print(n)
    if count == 1:
        print(f'Ход игрока {gamer_2}.')
        g = digi()
        n = n - g
        count == 0
        print(f'Остаток {n}')
    
    if n > 28:
        # gamer_2 == gamer_1
        # gamer_1 = gamer_2
        return util(n)
    if n < 29:
        return print(f'Выиграл игрок {gamer_1}. Поздравляем!!!')

    
util(2021)  

#-----------------------------------------------------------
exit()
import random

def draw():
    gamer_man = 'Человек'
    gamer_bot = 'Бот'
    
    print('\nДля определения очередности хода бросаем жребий: \n')
    lot_1 = input(f'Жребий бросает игрок {gamer_man}.\nЧтобы сделать ход нажмите "ENTER": ')
    
    if lot_1 == '':
        n_1 = random.randint(1, 3)
        print(f'Игроку {gamer_man} выпало число: {n_1}\n')

    print(f'Жребий бросает игрок {gamer_bot}.')
    n_2 = random.randint(1, 3)
    print(f'Игроку {gamer_bot} выпало число: {n_2}\n')
    
    if n_1 == n_2:
        print(input('Ничья. Пребросьте жребий.\nДля продолжения нажмите "ENTER": '))
        return draw()
    elif n_1 > n_2:
        winner_draw = gamer_man
        print(f'Число {n_1} больше {n_2}. \nИгру начинает игрок {winner_draw}.\n')
    else:
        winner_draw = gamer_bot
        print(f'Число {n_2} больше {n_1}. \nИгру начинает игрок {winner_draw}.\n')
        print(f'ВИННЕР {winner_draw}')       
    return winner_draw
       
def digi():
    gi = input('Введите число на хрен: ')
    if not gi.isdigit():
        print('Неверно. Повторите.')
        return digi()
    elif int(gi) <= 0 or int(gi) > 1000:
        print('Неверно. Повторите.')
        return digi()
    else:
        return int(gi)
    
gamer_ = draw()
print(gamer_)

def util(n):
    gamer_1 = gamer_
    gamer_2 = ''
    if gamer_1 == 'Человек':
        gamer_2 == 'Бот'
    elif gamer_1 == 'Бот':
        gamer_2 = 'Человек'

    print(f'Ход игрока {gamer_1}.')
    g = digi()
    n = n - g
    print(n)
    print(f'Ход игрока {gamer_2}.')
    g = digi()
    n = n - g
    print(f'Остаток {n}')
    if n > 28:
        gamer_2 == gamer_1
        return util(n)
    if 1 < n < 29:
        return print(f'Выиграл игрок {gamer_1}. Поздравляем!!!')

util(2021)  

# from random import *
# import os


# welcome_text = ('Приветствую Вас, маленькие любители сладкого!\n'
#                 'Хотите сыграть в игру "2021 шаг в сторону сахарного диабета"?\n'
#                 'Для начала я расскажу правила:\n'
#                 'Я даю Вам 2021 конфету, вы берете их поочереди,\n'
#                 'причем, за один раз можно взять не больше 28 конфет.\n'
#                 'Выигрывает тот, кто последним ходом заберет все конфеты.\n'
#                 'Ну что начнем?')
# print(welcome_text)

# message = ['твоя очередь', 'да бери уже', 'бери больше', 'не корову проигрываешь',
#            'бери быстрее', 'да харош, так долго думать уже']


# def player_vs_player():
#     candies_total = 2021
#     max_take = 28
#     count = 0
#     player_1 = input('\nКак тебя зовут?: ')
#     player_2 = input('\nА твоего соперника?: ')

#     print(f'\nНу чтож {player_1} и  {player_2} да начнется игра !\n')
#     print('\nДля начала опеределим кто первый начнет игру.\n')

#     x = randint(1, 2)
#     if x == 1:
#         lucky = player_1
#         loser = player_2
#     else:
#         lucky = player_2
#         loser = player_1
#     print(f'Поздравляю {lucky} ты ходишь первым !')

#     while candies_total > 0:
#         if count == 0:
#             step = int(input(f'\n{choice(message)} {lucky} = '))
#             if step > candies_total or step > max_take:
#                 step = int(input(
#                     f'\nНе жадничай можно взять только {max_take} конфет {lucky}, попробуй еще раз: '))
#             candies_total = candies_total - step
#         if candies_total > 0:
#             print(f'\nна кону еще {candies_total}')
#             count = 1
#         else:
#             print('Все кончились конфетки')

#         if count == 1:
#             step = int(input(f'\n{choice(message)}, {loser} '))
#             if step > candies_total or step > max_take:
#                 step = int(input(
#                     f'\nНе жадничай можно взять только {max_take} конфет {loser}, попробуй еще раз: '))
#             candies_total = candies_total - step
#         if candies_total > 0:
#             print(f'\nна кону еще {candies_total}')
#             count = 0
#         else:
#             print('Баста, карапузик, кончились конфетки')

#     if count == 1:
#         print(f'{loser} ПОБЕДИЛ')
#     if count == 0:
#         print(f'{lucky} ПОБЕДИЛ')


# player_vs_player()


# def player_vs_bot():
#     candies_total = 2021
#     max_take = 28
#     player_1 = input('\nКак тебя зовут?: ')
#     player_2 = 'Компьютер'
#     players = [player_1, player_2]
#     print(f'\nНу чтож {player_1} и  {player_2} да начнется игра !\n')
#     print('\nДля начала опеределим кто первый начнет игру.\n')

#     lucky = randint(-1, 0)

#     print(f'Поздравляю {players[lucky+1]} ты ходишь первым !')

#     while candies_total > 0:
#         lucky += 1

#         if players[lucky % 2] == 'Компьютер':
#             print(
#                 f'\nХодит {players[lucky%2]} \nНа кону {candies_total}. \n{choice(message)}: ')

#             if candies_total < 29:
#                 step = candies_total
#             else:
#                 delenie = candies_total//28
#                 step = candies_total - ((delenie*max_take)+1)
#                 if step == -1:
#                     step = max_take -1
#                 if step == 0:
#                     step = max_take
#             while step > 28 or step < 1:
#                 step = randint(1,28)
#             print(step)
#         else:
#             step = int(input(f'\nНу чтож ходи,  {players[lucky%2]} \nНа кону {candies_total} {choice(message)}:  '))
#             while step > max_take or step > candies_total:
#                 step = int(input(f'\nЗа один ход можно взять {max_take} конфет, попробуй еще раз: '))
#         candies_total = candies_total - step

#     print(f'На кону осталось {candies_total} \nПобедил {players[lucky%2]}')

# player_vs_bot()

