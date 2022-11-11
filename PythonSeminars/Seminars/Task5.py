 # import re

# result = re.match(r'AV', 'AV Analytics Vidhya AV')
# print(result.group(0))

# result = re.match(r'AV', 'AV Analytics Vidhya AV')
# print (result.start())
# print (result.end())


# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

def rle_encode(data):
    encoding = '' 
    prev_char = '' 
    count = 1 

    if not data: return ''

    for char in data:
        # If the prev and current characters don't match... 
        if char != prev_char: 
        # ...then add the count and character to our encoding 
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            # Or increment our counter if the characters do match 
            count += 1 
    else: 
        # Finish off the encoding 
        encoding += str(count) + prev_char 
        return encoding
encoded_val = rle_encode('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE')
print(encoded_val)


# data = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
# fir = data[0]
# count = 1
# for fur in data:
#     if fur != fir:
#         count = 1
#     if fur == fir:
#         count +=1
#         print(count)
#     else:
#         fur = data[]
#     else:
#         print(fir + str(count))

#     print(fir)


# def rle_encode(data):
#     encoding = '' 
#     prev_char = '' 
#     count = 1

#     if not data: return ''

#     for char in data:
#         if char != prev_char: 
#             if prev_char: 
#                 encoding += str(count) + prev_char 
#             count = 1
#             prev_char = char 
#         else: 
#             count += 1 
#     else: 
#         encoding += str(count) + prev_char 
#         return encoding
    
# encoded_val = rle_encode('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE')
# print(encoded_val)

import random

def step():
    num = input('Введите число на хрен: ')
    if not num.isdigit():
        print('Неверно. Повторите.')
        return step()
    elif int(num) <= 0 or int(num) > 28:
        print('Неверно. Повторите.')
        return step()
    else:
        return int(num)

def draw(n):
    gamer_man = 'Человек'
    gamer_bot = 'Бот'
    count = 0
    winner_draw = ''
    looser_draw = ''   
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
    elif n_1 > n_2:
        winner_draw = gamer_man
        looser_draw = gamer_bot
        print(f'Число {n_1} больше {n_2}. \nИгру начинает игрок {winner_draw}.\n')
    else:
        winner_draw = gamer_bot
        looser_draw = gamer_man
        print(f'Число {n_2} больше {n_1}. \nИгру начинает игрок {winner_draw}.\n')
    
    
    while n > 29:
        if count == 0:
            print(f'Ход игрока {winner_draw}.')
            g = digi()
            n = n - g
            print(f'Остаток QW {n}')
            count = 1
        else: 
            'Конец 1'
            
        if count == 1:
            print(f'Ход игрока {looser_draw}.')
            g = digi()
            n = n - g
            print(f'Остаток {n}')
            count = 0
        else:
            'Конец 2'
    if n <= 28:        
        if count == 0:
            return print(f'Выиграл игрок {winner_draw}. Поздравляем!!!')
        if count == 1:
            return print(f'Выиграл игрок {looser_draw}. Поздравляем!!!')
 
draw(100)  

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