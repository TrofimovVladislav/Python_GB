# задача 3. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random

# k = 3
# for i in range(3):
#     a = random.randint(0,100)
#     chlen = (f'{a}*x^{k} + {a}*x^{k} + {a} = 0')
    
#     k=k-1
#     print(chlen)

# from random import randint
# max_val=100
# k = int(input('Введите натуральную степень k: '))
# # # коэфф. при старшей степени не должен быть равен 0
# koeff=[randint(0,max_val) for i in range(k)]+[randint(1,max_val)]
# poly='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(koeff) if j][::-1])
# # Поиск и замены:
# poly=poly.replace('x^1+', 'x+')
# poly=poly.replace('x^0', '')
# poly = poly + ('','1')[poly[-1]=='+']
# poly = (poly, poly[:-2])[poly[-2:]=='^1']
# print(f'\n{poly}\n')

# print(poly)


# seq = list('абвгде')

# # ['а', 'б', 'в', 'г', 'д', 'е']
# for i, val in enumerate(seq, start=1):
#     print(f'№ {i} => {val}')

# № 1 => а
# № 2 => б
# № 3 => в
# № 4 => г
# № 5 => д
# № 6 => е

# from random import randint
 
# print('Введите натуральную степень k:')
# k = int(input())
 
# def write_file(st):
#     with open('Task04.txt', 'w') as data:
#         data.write(st)
 
# def create_list(k):
#     list = []
#     for i in range(k + 1):
#         list.append(randint(0, 101))    
#     return list
    
# def create_str(sp):
#     list = sp[::-1]
#     wr = ''
#     if len(list) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(list)):
#             if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
#                 wr += f'{list[i]}x^{len(list) - i - 1}'
#                 if list [i + 1] != 0:
#                     wr += ' + '
#             elif i == len(list) - 2 and list[i] != 0:
#                 wr += f'{list[i]}x'
#                 if list[i + 1] != 0:
#                     wr += ' + '
#             elif i == len(list) - 1 and list[i] != 0:
#                 wr += f'{list[i]} = 0'
#             elif i == len(list) - 1 and list[i] == 0:
#                 wr += ' = 0'
#     return wr
 
# koef = create_list(k)
# write_file(create_str(koef))

# from random import randint

# k = 5
# kf = []; wert = []; zf = []
# if k == 0: print('her')
# else: 
#     for i in range(k):
#         kf.append(randint(0, 5))
#     for j in range(k):
#         wert.append(f'{kf[j]}x^{k}')
#         k = k-1
#         qw = f'{" + ".join(wert)}' ' + ' f'{randint(1,100)} = 0'
        
#     qw = qw.replace('x^1', 'x')
#     qw = qw.replace('1x^', 'x^')
#     qw = qw.replace('1x', 'x')
#     qw = qw.replace('0x + ', '')
#     qw = qw.replace(f'0x^{k}', '')

#     print(qw)

# from random import randint
# def hren():
#     k = 2
#     kf = []; wert = []; zf = []
#     if k == 0: print('her')
#     else: 
#         for i in range(k):
#             kf.append(randint(0, 100))
#             if kf[i] != 0:
#                 zf.append(kf[i])
#                 k = len(zf)
#         i = i + 1    
#         for j in range(k):
#             wert.append(f'{zf[j]}x^{k}')
#             k = k-1

#         fg = randint(0, 100)
#         if fg == 0: fg = ''
#         qw = f'{" + ".join(wert)}' ' + ' f'{fg}  = 0'
    
#         qw = qw.replace(' +  ', '') 
#         qw = qw.replace('x^1', 'x')
#         qw = qw.replace('1x^', 'x^')
#         qw = qw.replace('1x', 'x')
#         qw = qw.replace('0x + ', '')
           
#     # print(qw)
#     return qw
# print(hren())
# print(hren())
# print(hren())
# print(hren())
# print(hren())
# print(hren())

# import random
 
# res = []
# for n in range(7):
#     if n not in res:
#         res.append(random.randint(1,50))
# print (res)

# СПИСКИ ----------------------------------------

# sp = []
# sp.append(True)
# sp = sp + [1213, 'abba', 54654, [1, 2, 3, 5]]
# print(sp)

# sp.insert(0, 999)
# print('after append', sp)

# a = sp.pop(-1)
# print('after pop', a)
# a.remove(2)
# print('after remove', a)

# for i in a: print(i)

# mas_2dim = []
# for i in range(5):
#     temp = []
#     for j in range(5):
#         temp.append(i + j)
#     mas_2dim.append(temp)

# for i in range(len(mas_2dim)):  # для печати в столбик
#     print(mas_2dim[i])

# СЛОВАРИ ---------------------------------------

# book = {}

# book['Миша'] = 98465566
# book['Саша']=[64654464,46546464]

# print(book)

# if 'Даша' in book: 
#     print("Yes")
# else: 
#     print("No")

# for x,y in book.items():
#     print(x, y)

# for x in book.values():
#     print(x)

# for x in book.keys():
#     print(x)

# 1. Напишите программу, которая принимает на вход число N и 
# выдаёт последовательность из N членов.

# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81

# import math

# def any_math():
#     try:
#         n = int(input('Введите число: '))
#         for i in range(n):
#             print(math.pow(-3, i), end = ' ')
#     except:
#         print('Введены некоректные данные повторите ввод.')
#         return any_math()
    
# any_math()



# 2. Для натурального n создать словарь индекс-значение, 
# состоящий из элементов последовательности 3n + 1.

# *Пример:*

# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
import random
n = int(input('Введите n: '))
book = {}
# los = ['козел', 'не козел', 'кот', 'не кот', 'собака', 'не собака']
for i in range(n):
    book[i+1] = 3*(i+1) + 1
    # book[i+1] = random.choice(los)

print(book, end='\n')

# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

# sp1 = 'аброкадабра аброкдабра'
# sp2 = 'бр'

# # x = sp.count(sp1)
# # print(x)

# count = 0
# for i in range(len(sp1)):
#     if sp1[i: i+len(sp2)] == sp2:
#         count = count + 1
       
# print(count) 




    
