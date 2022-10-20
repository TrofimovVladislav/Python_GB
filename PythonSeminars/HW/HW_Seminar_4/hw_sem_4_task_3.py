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
# kf = []; wert = []
# if k == 0: print('her')
# else: 
#     for i in range(8):
#         kf.append(randint(0, 5))
#     for i in range(k):
#         wert.append(f'{kf[i]}x^{k}')
#         k = k-1
        
#         qw = f'{" + ".join(wert)}' ' + ' f'{randint(1,100)} = 0'
        
#     qw = qw.replace('x^1', 'x')
#     qw = qw.replace('0x + ', '')
#     qw = qw.replace(f'0x^{k}', '')

#     print(qw)
    
from random import randint

k = 5
kf = []; wert = []
# kf.append(randint(0, 3))
if k == 0: print('her')
else: 
    for i in range(8):
        kf.append(randint(0, 3))
        if kf[i]!=0:
            print(f'i{i} {kf[i]}')
            # kf.append(randint(0, 5))
        i=i+1
            # kf.append(randint(0, 5))
            
    # for j in range(k):
    #     wert.append(f'{kf[j]}x^{k}')
    #     k = k-1
    
    # qw = f'{" + ".join(wert)} + {randint(1,100)} = 0'
           
    # qw = qw.replace('x^1', 'x')
    # qw = qw.replace('0x + ', '')
    # qw = qw.replace('1x + ', 'x')
    # qw = qw.replace('1x', 'x')
    # # qw = qw.replace(f'0x^', '')

    # print(qw)
    
    




    

        
