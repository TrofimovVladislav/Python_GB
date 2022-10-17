# Задача 1. Напишите программу, которая принимает 
# на вход вещественное или целое число и показывает
# сумму его цифр. Через строку нельзя решать.

# *Пример:*

# - 67,82 -> 23
# - 0,56 -> 11
# - 456536

def check_any_digit():
    """
    Функция проверяет является ли введенное 
    значение целым или вещественным числом.
    """
    input_data = input('Введите число: ')
    if input_data.isdigit():
        return input_data
    elif any(input_data.replace(x,'').isdigit() for x in ('.',',','-')):
        return input_data
    else:
        print(f'Вы ввели не число.\nПовторите ввод. ')
        return check_any_digit()
  

def float_figures_sum():
    """
    Функция находит сумму цифр целого или вещественного числа.
    """
    # num = input('\nВведите число: ')
    num_abs = check_any_digit()
    sum = 0
    for i in num_abs:
        if i != '.' and i != ',' and i != '-':
            sum += int(i)
    print(f'Сумма всех цифр числа {num_abs} равна {sum}.')

# # float_figures_sum(67.82)
# # float_figures_sum(0.56)
# # float_figures_sum(456536)
float_figures_sum()



