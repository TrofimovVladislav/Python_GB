# К задаче из Семинара 3

# from random import *

# pred = [True, False]
# kolvo = randint(5,25)
# predicates = [choice(pred) for _ in range(kolvo) ]

# print(predicates)

# Семинар 4 -------------------------------------

# import json

# BD={'Иванов': { 'adress':'MSK center', 'e-mail': 'sdfsfsf@ssdfsdf.ru' ,
import json

# BD = {'Иванов': { 'adress':'MSK center', 'e-mail': 'sdfsfsf@ssdfsdf.ru' ,
# 'phones': [654644464,6546465646,464566465,86465464465] } }

# def load():
# # загрузить из json
#     fname = 'BD.json' #открываем файл
#     with open(fname, 'r', encoding='utf-8') as fh: # открываем файл на чтение
#         BD_local = json.load(fh) # загружаем из файла данные в словарь data
<<<<<<< HEAD
#         print('БД успещно загружена')
#         return BD_local
=======
#     print('БД успещно загружена')
#     return BD_local
>>>>>>> 4ba9f98c48a30d1e8d26ab0d3af4214f50490a60

# def save():
# # сохранить в json
#     with open('BD.json', 'w', encoding='utf-8') as fh: # открываем файл на запись
#         fh.write(json.dumps(BD, ensure_ascii=False)) # преобразовываем словарь data в unicode-строку и записываем в файл
#         print('БД успещно сохранена')

# save()


# BDnew = load ()
# print(BDnew)

<<<<<<< HEAD
=======

#------------------------------------------------
>>>>>>> 4ba9f98c48a30d1e8d26ab0d3af4214f50490a60
# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

<<<<<<< HEAD
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
=======
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# Вариант 1

# number = int(input("Введите целое число: "))
# list_pos = [0, 1]
# list_neg = [0, 1]
# for i in range(number-1):
#     list_pos.append(list_pos[-1] + list_pos[-2])
#     list_neg.append(list_neg[-2] - list_neg[-1])

# list_result = list_neg[::-1] + list_pos[1:]
# print(list_result)

# Вариант 2

# num = int(input("Введите количество членов ряда Негафибоначчи: "))
# result =[1, 0, 1]
# while num!=1:
#     k = (result[-1]+result[-2])
#     result.append(k)
#     result.insert(0, (-1)**(num+1)*k)
#     num-=1
# print(result)

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 ) с 
# помощью математических формул нахождения корней квадратного уравнения


# try:
#     A = int(input('Введите значение коэффициента A: '))
#     B = int(input('Введите значение коэффициента B: '))
#     C = int(input('Введите значение коэффициента C: '))
# except:
#     'HER'
    


# def quadratic_equation(A, B, C):

#     D = B*B - 4*A*C
    
#     if D > 0:
#         x1 = (-B + D**0.5)/(2*A)
#         x2 = (-B - D**0.5)/(2*A)
#         print(f'Выражение имеет два корня {x1} и {x2}.')
#     elif D == 0:
#         x1 = -B/(2*A)
#         print(f'Выражение имеет один корень {x1}.')
#     else:
#         print(f'Выражение не имеет корней.')

# quadratic_equation(A, B, C)


# 3. Задайте два числа. Напишите программу, которая найдёт НОК 
# (наименьшее общее кратное) этих двух чисел.

# a = 126
# b = 70
def nod(a,b):
    while a%b > b:
        a%b
    d = a%b
    # print(f'd {d}')
   
    while b%d > d:
        b%d
    z = b%d
    print(f'z {z}')
    nok = (a*b)/z
    print(nok)
    return nok

nod(300, 23)



# print(252%70)
# print(70%56)
# print(56%14)
# print((126*70)/14)
>>>>>>> 4ba9f98c48a30d1e8d26ab0d3af4214f50490a60
