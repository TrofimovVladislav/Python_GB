# К задаче из Семинара 3

# from random import *

# pred = [True, False]
# kolvo = randint(5,25)
# predicates = [choice(pred) for _ in range(kolvo) ]

# print(predicates)

# Семинар 4 -------------------------------------

# import json

# BD={'Иванов': { 'adress':'MSK center', 'e-mail': 'sdfsfsf@ssdfsdf.ru' ,
# 'phones': [654644464,6546465646,464566465,86465464465] } }

# def load():
# # загрузить из json
#     fname = 'BD.json' #открываем файл
#     with open(fname, 'r', encoding='utf-8') as fh: # открываем файл на чтение
#         BD_local = json.load(fh) # загружаем из файла данные в словарь data
#         print('БД успещно загружена')
#         return BD_local

# def save():
# # сохранить в json
#     with open('BD.json', 'w', encoding='utf-8') as fh: # открываем файл на запись
#         fh.write(json.dumps(BD, ensure_ascii=False)) # преобразовываем словарь data в unicode-строку и записываем в файл
#         print('БД успещно сохранена')

# save()


# BDnew = load ()
# print(BDnew)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: 
#     [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


# n = 5
# fib = [0, 1]
# # res = []

# for i in range(1, n):
#     sum = fib[i+2] - fib[i+1]
#     fib.append(sum)
    
# print (fib)   

# x = int(input("Введите число: "))
# y = int(input("Введите число: "))

# big_num = max(x, y)

# while True:
#     if big_num % x == 0 and big_num % y == 0:
#         result =  big_num
#         break
#     big_num += 1
# print(big_num)

    
we = []
s = '-27x2-6x-18=0'
for i, j in enumerate(s):
    if 'x' == j: 
        we.append(i)
    elif '=' == j:
        we.append(i)
a = int(s[:we[0]])
b = int(s[we[0]+2:we[1]])
c = int(s[we[1]+1:we[2]])

print(a, b, c)
