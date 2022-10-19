# Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z . 
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25, сами значения предикатов случайные, 
# проверяем это утверждение 100 раз, с помощью модуля time выводим на экран , сколько времени отработала программа.

# import time

# def Truth ():
#     result = True
#     start = time.time()

#     for n in range (0, 100):
#         num = bin(n)
#         print(num)
#         num = num.replace('b', '0')
#         X = int(num[-3])
#         # print(X)
#         Y = int(num[-2])
#         # print(Y)
#         Z = int(num [-1])
#         # print(Z)
#         result = (not(X or Y or Z)) == ((not X) and (not Y) and (not Z))
#         end = time.time()
#     print (result)
#     print(f'Время выполнения программы {end-start} сек')


# Truth ()


import random

# predict_lib = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# n = random.randint(5, 6)
# pred_1 = random.sample(predict_lib, n)
# g = ('not '  + ' and' ' not '.join(pred_1))
# print(g)
# t = ' or '.join(pred_1)
# print(t)
# result = not(t) == g
# print(result)


import string

letters = string.ascii_uppercase
rand_string = ' '.join(random.sample(letters, 3))
print(rand_string)
i=0
rand_string[0] = random.randint(0,2)
print(rand_string[i])


# for i in range(lenf-1):
#     rand_string = i
#     print(rand_string)
# n = random.randint(0,1)
# print(n)
