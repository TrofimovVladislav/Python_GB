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

def check_int(max_num_candy):
    num = input('Введите количество забираемых конфет: ')
    if not num.isdigit():
        print(f'Ошибка. Введите число от 1 до {max_num_candy}.')
        return check_int(max_num_candy)
    num = int(num)
    if num <= 0 or num > max_num_candy:
        print(f'Ошибка. Введите число от 1 до {max_num_candy}.')
        return check_int(max_num_candy)
    else:
        return num
    
def candy_game(candy_num, max_num_candy):
    gamer_man = 'Человек'
    gamer_bot = 'Бот'
    count = 0
        
    print('Для определения очередности хода бросаем жребий.')
    lot_1 = input(f'Жребий бросает игрок {gamer_man}.\nЧтобы сделать ход нажмите "ENTER": ')
    
    if lot_1 == '':
        draw_1 = random.randint(1, 3)
        print(f'Игроку {gamer_man} выпало число: {draw_1}.\n')
        
    print(f'Жребий бросает игрок {gamer_bot}.')
    draw_2 = random.randint(2, 6)
    print(f'Игроку {gamer_bot} выпало число: {draw_2}.\n')
    
    if draw_1 == draw_2:
        print(input('Ничья. Пребросьте жребий.\nДля продолжения нажмите "ENTER": '))
        return candy_game(candy_num, max_num_candy)
                
    if draw_1 > draw_2:
        winner_draw = gamer_man
        loser_draw = gamer_bot
        print(f'Число {draw_1} больше чем {draw_2}')
    else:
        if draw_2 > draw_1:
            winner_draw = gamer_bot
            loser_draw = gamer_man
            print(f'Число {draw_2} больше {draw_1}')
    print(f'Первым ходит игрок {winner_draw}.\n')

    while candy_num > max_num_candy + 1:
        
        if count == 0:
            print(f'Ход игрока {winner_draw}.')
            
        if winner_draw == 'Человек':
            step = check_int(max_num_candy)
            candy_num = candy_num - step
            print(f'Человек взял {step} конфет.\nОсталось {candy_num} конфет.\n')
            if candy_num > max_num_candy:
                count = 1
            else:
                break
        else:
            step = random.randint(1, max_num_candy + 1)
            candy_num = candy_num - step
            print(f'Бот взял {step} конфет.\nОсталось {candy_num} конфет.\n')
            if candy_num > max_num_candy:
                count = 1
            else:
                break
                      
        if count == 1:
            print(f'Ход игрока {loser_draw}.')
            
        if loser_draw == 'Бот':
            step = random.randint(1, max_num_candy + 1)
            candy_num = candy_num - step
            print(f'Бот взял {step} конфет.\nОсталось {candy_num} конфет.\n')
            if candy_num > max_num_candy:
                count = 0
            else:
                break
        else:
            step = check_int(max_num_candy)
            candy_num = candy_num - step
            print(f'Человек взял {step} конфет.\nОсталось {candy_num} конфет.\n')
            if candy_num > max_num_candy:
                count = 0
            else:
                break
              
    if count == 0:
        print(f'Выигарл игрок {loser_draw}. Поздравляем!!!')
    if count == 1:
        print(f'Выиграл игрок {winner_draw}. Поздравляем!!!')

candy_game(50, 10)