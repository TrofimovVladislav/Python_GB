# Задача 4. Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное. Нельзя использовать готовые функции.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decimal_to_binary(num):
    '''
    Функция преобразовывает число из десятичной в двоичную систему счисления.
    '''
    # input_num = ('Введите десятичное число: ')
    input_num = num
    binary_num = ''
    while num > 0:
        binary_num = str(num % 2) + binary_num
        num = num // 2
    
    print(f'Результат перевода десятичного числа ({input_num}) в двоичное: {binary_num}')

    return binary_num
    
decimal_to_binary(45)
decimal_to_binary(3)
decimal_to_binary(2)
