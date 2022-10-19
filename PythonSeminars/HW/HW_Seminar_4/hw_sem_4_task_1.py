# задача 1. Задайте натуральное число N. 
# Напишите программу, которая составит список 
# простых множителей числа N.

# def check_int():
#     """
#     Функция проверяет является ли введенное значение числом.
#     """
#     input_data = input('Введите число: ')
#     if not input_data.isdigit():
#         print(f'Вы ввели не число.\nПовторите ввод. ')
#         return check_int()
#     else:
#         return input_data

def simple_multiplier(num):
    '''
    Функция находит простые множетили числа.
    '''
    i = 2
    input_num = num
    list_simple = list()
    while num > 1:
        if num % i == 0:
            if i not in list_simple:
                list_simple.append(i)
            num = num // i
        else:
            i = i+1
    print(f'Простые множители числа ({input_num}): {list_simple}')
    
    return list_simple
           
# simple_multiplier()
simple_multiplier(31)
simple_multiplier(618)
simple_multiplier(97)



