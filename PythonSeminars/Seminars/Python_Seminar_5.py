# задача 4 необязательная Даны два многочлена. 
# Задача - сформировать их сумму.

# например, 5*x^3 + 2*x^2 + 6 и 7*x^2 + 6*x + 3 , 
# Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9

# pol_1 = '5*x^3 + 14*x^2 + 6'
# pol_2 = '7*x^2 + 6*x + 3'



# print(pol_1 + pol_2)
# pol_0 = (pol_1 + pol_2)

# pol_3 = ''
# for i in pol_0:
#     print(i)
    # if 'x^2' in i:
    #     pol_3.append(i)
    #     print(pol_3)
        # pol_3.remove('*x^2')
        # print(pol_3)

# for i in pir_1:
#     if 'x^2' in i:
        
#         print(i[:])
#         sum = (int(i[:1]) + int(i[:1]))
        # print(sum)
        

    # if 'x^2' in i:
    #     print(pir_1[0])
# for j in pir_2:
#     if 'x^2' in j:
#         print(j)
        
# print(i[0])

# pol = '5*x^3 + 14*x^2 + 6 = 0'

import re
import itertools


file_1 = 'C:/GB/Python_GB/PythonSeminars/HW/HW_Seminar_5/33_Polynomial.txt'
file_2 = 'C:/GB/Python_GB/PythonSeminars/HW/HW_Seminar_5/33_Polynomial2.txt'
# file2 = '33_Polynomial2.txt'
file_sum = '34_Sum_polynomials.txt'

# Получение данных из файла

def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

# Получение списка кортежей каждого (<коэффициент>, <степень>)

def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol

# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)

def fold_pols(pol1, pol2):   
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

# Составление итогового многочлена

def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

pol1 = read_pol(file_1)
pol2 = read_pol(file_2)
pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)

pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
# print(pol_sum)
# write_to_file(file_sum, pol_sum)

print(pol1)
print(pol2)
print(pol_sum)

#------------------------------------------------

# задача 5 необязательная Дан список чисел. 
# Создайте список, в который попадают числа, 
# описывающие максимальную возрастающую последовательность. 
# Порядок элементов менять нельзя.

# *Пример:*


# nums1 = [1, 5, 2, 3, 4, 6, 1, 7] #=> [1, 7]
# nums2 = [1, 5, 2, 3, 4, 1, 7]    #=> [1, 5]


def find_list(start_num, current_list):
    new_list = [start_num]
    max_num = max(current_list)

    for k in range(start_num, max_num):
        if start_num + 1 in current_list:
            new_list.append(start_num + 1)
            start_num += 1
                       
    if len(new_list) > 1:
        return new_list

    return []

list_of_numbers = [1, 5, 3, 2, 4, 1, 7]
lists = []
min_num = min(list_of_numbers)

current_list = find_list(min_num, list_of_numbers)
print(current_list)



# def max_sequence(seq):
#     temp = []
#     res = []
#     nums_max = max(seq)
#     nums_max_index = enumerate([nums_max])
#     for i, el in enumerate(seq):
#         if el == nums_max:
#             nums_max_index = i
#     for i in range(nums_max_index):
#         if seq[nums_max_index - i] < seq[nums_max_index]:
#             temp.append(seq[nums_max_index - i])
#             seq[nums_max_index] = seq[nums_max_index - i]
#     for j in reversed(temp):
#         res.append(j)
#     res.append(nums_max)
#     print(res)
#     return res

# max_sequence(nums1)
# max_sequence(nums2)


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