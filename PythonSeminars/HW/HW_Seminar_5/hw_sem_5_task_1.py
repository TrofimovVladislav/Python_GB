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

def candy_game(n, max_num_candy):
    candy_num = n
    gamer_man = 'Человек'
    gamer_bot = 'Бот'
    count = 0
        
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
    if n_1 > n_2:
        winner_draw = gamer_man
        loser_draw = gamer_bot
    else:
        winner_draw = gamer_bot
        loser_draw = gamer_man
    print(f'Первым ходит игрок {winner_draw}.')

    while candy_num > max_num_candy + 1:
        if count == 0:
            step = int(input(f'Ход игрока {winner_draw}: '))
            if step > candy_num or step > max_num_candy:
                step = int(input(f'За один ход можно взять не больше {max_num_candy} конфет. Повторите ход: '))
            candy_num = candy_num - step
        if candy_num > max_num_candy + 1:
            print(f'Осталось еще {candy_num} конфет.')
            count = 1
      
        if count == 1:
            step = int(input(f'Ход игрока {loser_draw}: '))
            if step > candy_num or step > max_num_candy:
                step = int(input(f'За один ход можно взять не больше {max_num_candy} конфет. Повторите ход: '))
            candy_num = candy_num - step
        if candy_num > max_num_candy + 1:
            print(f'Осталось еще {candy_num} конфет.')
            count = 0
  
    if count == 0:
        print(f'Выигарл игрок {loser_draw}. Поздравляем!!!')
    if count == 1:
        print(f'Выиграл игрок {winner_draw}. Поздравляем!!!')


candy_game(2021, 28)

