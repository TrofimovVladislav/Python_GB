# 1. Напишите программу, которая принимает на вход два числа 
# и проверяет, является ли одно число квадратом другого.

# *Примеры:*

# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет


def check_int(msg):
    input_data = input(msg)
    if not input_data.isdigit(): 
        return check_int("Вы ввели не число.\nВведите число: ")
    else:
        return input_data
   
def sert():
    num_1 = check_int('Введите число: ')
    num_2 = check_int('Введите число: ')
     
    num_1 = int(num_1)
    num_2 = int(num_2)
    
    if num_1 >= num_2 and num_1 ** 0.5 == num_2:
        print('Да')
    if num_1 <= num_2 and num_2 ** 0.5 == num_1:
        print('Да')
    else:
        print('Нет')
        
sert()
    
    
