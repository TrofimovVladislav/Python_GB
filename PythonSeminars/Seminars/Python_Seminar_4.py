import json

# BD = {'Иванов': { 'adress':'MSK center', 'e-mail': 'sdfsfsf@ssdfsdf.ru' ,
# 'phones': [654644464,6546465646,464566465,86465464465] } }

# def load():
# # загрузить из json
#     fname = 'BD.json' #открываем файл
#     with open(fname, 'r', encoding='utf-8') as fh: # открываем файл на чтение
#         BD_local = json.load(fh) # загружаем из файла данные в словарь data
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
        if a%b == 0:
            d = b
        else:
            a%b
    d = a%b
    print(f'd {d}')
   
    while b%d > d:
        b%d
        if b%d == 0:
            z = d
        else:
            z = b%d
    print(f'z {z}')
    nok = (a*b)/z
    print(nok)
    return nok

nod(68, 34)



# print(252%70)
# print(70%56)
# print(56%14)
# print((126*70)/14)
