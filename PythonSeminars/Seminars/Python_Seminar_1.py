# 1. Напишите программу, которая принимает на вход два числа 
# и проверяет, является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет


# def check_int(msg):
#     input_data = input(msg)
#     # print(type(input_data))
#     if not input_data.isdigit(): 
#         return check_int("Вы ввели не число.\nВведите число: ")
#     else:
#         return input_data
    
# # check_int()
   
# def check_square():
#     num_1 = check_int('\nВведите первое число: ')
#     num_2 = check_int('Введите второе число: ')
     
#     num_1 = int(num_1)
#     num_2 = int(num_2)
    
#     if num_1 ** 0.5 == num_2:
#         print(f'\nЧисло {num_1} является квадратом числа {num_2}.\n')
#     elif num_2 ** 0.5 == num_1:
#         print(f'\nЧисло {num_2} является квадратом числа {num_1}.\n')
#     else:
#         print(f'\nЧисла {num_1} и {num_2} не являются квадратом друг друга.\n')
        
# check_square()
mas = [[2, 4, 7, 3], [4, 5, 6, 9], [1, 0, 4, 2], [7, 8, 4, 7]]
mas2 = []
for i in mas:
    for i2 in i:
        mas2.append(i2)
mas=sorted(mas2)
for x in range(0, len(mas), 4):
    e_c = mas[x : 4 + x]
    if len(e_c) < 4:
        e_c = e_c + [None for y in range(n - len(e_c))]
    print(list(e_c))




    
    
