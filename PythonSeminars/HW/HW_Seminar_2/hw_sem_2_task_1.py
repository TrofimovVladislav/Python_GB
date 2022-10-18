# Задача 1. Напишите программу, которая принимает 
# на вход вещественное или целое число и показывает
# сумму его цифр. Через строку нельзя решать.

# *Пример:*

# 67.82 -> 23
# 0,56 -> 11
# 4569 -> 24
# -4569.32 -> 29 

def check_any_digit():
    """
    Функция проверяет является ли введенное значение целым или вещественным числом.
    """
    input_data = input('Введите число: ')
    input_data = input_data.replace('-','').replace('.','').replace(',','')
    if input_data.isdigit():
        return input_data
    else:
        print(f'Вы ввели не число.\nПовторите ввод. ')
        return check_any_digit()
  
def sum_of_digits():
    """
    Функция находит сумму цифр целого или вещественного числа.
    """
    number = check_any_digit()
    sum = 0
    for i in number:
        if i != '.' and i != ',' and i != '-':
            sum += int(i)
    print(f'Сумма всех цифр введенного числа равна {sum}.')

sum_of_digits()


