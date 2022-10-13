# 1-Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет


def check_int():
    """
    Функция проверяет является ли введенное значение числом.
    """
    input_data = input('Введите номер дня недели: ')
    if not input_data.isdigit():
        print(f'Вы ввели не число.\nПовторите ввод. ')
        return check_int()
    else:
        return input_data
   
def check_weekend():
    """
    Функция проверяет какому дню недели соответствует
    введенное число - рабочему или выходному.
    """
    num_day = check_int()
    num_day = int(num_day)
    
    if 0 < num_day <= 5:
        return print(f'Это рабочий день.')
    elif 6 <= num_day <= 7:
        return print(f'Это выходной день.')
    else:
        print (f'Такого дня недели нет.\nВведите число от 1 до 7.')
        check_weekend()
        return

check_weekend()


            
            
    
    
    
