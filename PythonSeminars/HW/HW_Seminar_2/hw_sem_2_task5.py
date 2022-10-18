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

con = list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ')
pred = ' or '.join(con)
print(pred)
# for x in range (6):
#     for i in pred:
#         print(i, end = '')

import random

# test_list = ["1", "2", "3", "4", "5", "6"]

print(random.sample(con, 3))




