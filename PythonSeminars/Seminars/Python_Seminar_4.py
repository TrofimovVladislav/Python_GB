# К задаче из Семинара 3

# from random import *

# pred = [True, False]
# kolvo = randint(5,25)
# predicates = [choice(pred) for _ in range(kolvo) ]

# print(predicates)

# Семинар 4 -------------------------------------

# import json

# BD={'Иванов': { 'adress':'MSK center', 'e-mail': 'sdfsfsf@ssdfsdf.ru' ,
# import json

# BD = {'Иванов': { 'adress':'MSK center', 'e-mail': 'sdfsfsf@ssdfsdf.ru' ,
# 'phones': [654644464,6546465646,464566465,86465464465] } }

# def load():
# # загрузить из json
#     fname = 'BD.json' #открываем файл
#     with open(fname, 'r', encoding='utf-8') as fh: # открываем файл на чтение
#         BD_local = json.load(fh) # загружаем из файла данные в словарь data
#         print('БД успещно загружена')
#         return BD_local
#     print('БД успещно загружена')
#     return BD_local

# def save():
# # сохранить в json
#     with open('BD.json', 'w', encoding='utf-8') as fh: # открываем файл на запись
#         fh.write(json.dumps(BD, ensure_ascii=False)) # преобразовываем словарь data в unicode-строку и записываем в файл
#         print('БД успещно сохранена')

# save()


# BDnew = load ()
# print(BDnew)


#------------------------------------------------
# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: 
#     [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

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

# def nod(a,b):
#     while a%b > b:
#         a%b
#     d = a%b
#     # print(f'd {d}')
   
#     while b%d > d:
#         b%d
#     z = b%d
#     print(f'z {z}')
#     nok = (a*b)/z
#     print(nok)
#     return nok

# nod(300, 23)

# x = int(input("Введите число: "))
# y = int(input("Введите число: "))

# big_num = max(x, y)

# while True:
#     if big_num % x == 0 and big_num % y == 0:
#         result =  big_num
#         break
#     big_num += 1
# print(big_num)


import re
def check_equation():
    equation_ = input('Введите квадратное уравнение в формате Ax2+Bx+C=0,\n'
                      'где коэффициенты уравнения А, В и С - целые числа.\n'
                      'и коэффициет А не равен 0!\n'
                      'Вводить ураврнение нужно без пробелов. Начните ввод: \n')

    pattern = r'[-+1-9x2]+[-+0-9x]+[-+0-9]=0'   #Ax2+Bx+C=0
    pattern = r'[-+1-9x2]=0'                    #Ax2=0
    pattern = r'[-+1-9x2]+[-+0-9]=0'            #Ax2+C=0
    pattern = r'[-+1-9x2]+[-+0-9x]=0'           #Ax2+Bx=0            
    
    match = re.fullmatch(pattern, equation_)

    if match is not None:
        print(f'Уравнение "{match.group()}" введено верно.')    
    else:
        print(f'Уравнеие "{equation_}" введено с не верно.\nБудьте внимательны и повторите ввод.')
    return equation_

# check_equation()

def quadratic_equation_from():
    s = check_equation()
    elem_index = []

    for i, j in enumerate(s):
        if j == 'x' or j == '=': 
            elem_index.append(i)
            
    a = int(s[:elem_index[0]])
    if a == 0:
        print('Коэффициент А не может быть равен 0.\nПовторите ввод.\n')
        return check_equation()
    b = int(s[elem_index[0] + 2:elem_index[1]])
    c = int(s[elem_index[1] + 1:elem_index[2]])
    
    d = b*b - 4*a*c
   
    if d > 0:
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
        print(f'Квадратное уравнение имеет два корня {x1} и {x2}.')
    elif d == 0:
        x1 = -b/(2*a)
        print(f'Квадратное уравнение имеет один корень {x1}.')
    else:
        print(f'Квадратное уравнение не имеет корней.')

quadratic_equation_from()

