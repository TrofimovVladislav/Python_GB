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
       
# draw()

def digi():
    gi = int(input('Введите число на хрен: '))
    return gi
# digi()

# exit()
gamer_ = draw()
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
    # n = n - g
    # print(n)
    if n > 28:
        gamer_2 == gamer_1
        return util(n)
util(2021)
    
#     else:
#         print('Все')
#     else:
#         gamer_2 = 'Бот'
#         print(f'Ход игрока {gamer_2}')
#         g = digi()
#         n = n - g
#         print(f'Остаток после хода Бот{n}')
#         return util(n)
      
#     else:
#         gamer_2 = 'Бот'
#         g = input(f'Ход игрока {gamer_2}. Введите число от 1 до 28: ')
#     print(f'Ход игрока {gamer_2}')
#     g = input(digi())
#     if  not g.isdigit():
#         print(f'Ошибка ввода. Повторите ввод.')
#         return digi()
#     # g = int(g)
#     if int(g) > 28:
#         print(f'Ошибка ввода. Введите число от 1 до 28.')
#         return digi()
#     else:
#         g = int(g)
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