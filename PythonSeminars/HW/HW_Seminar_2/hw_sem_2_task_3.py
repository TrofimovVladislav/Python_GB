# Задача 3. Напишите программу, в которой пользователь будет 
# задавать две строки, а программа - определять количество 
# вхождений одной строки в другой. Нельзя юзать find или count.

def count_input():
    """
    Функция подсчитывает количество 
    вхождений строки 1 в стороку 2.
    """
    # string_1 = input(str('Введите строку 1: '))
    # string_2 = input(str('Введите строку 2: '))
    string_1 = 'the sunlight from the sun is bright'
    string_2 = 'sun'
    len_string_2 = len(string_2)
    inputs = 0
    for i in range(len(string_1)):
        if string_1[i : i+len_string_2] == string_2:
            inputs += 1
    print(f'\nКоличество вхождений строки "{string_2}" в строку \n"{string_1}" = {inputs}\n')
    return inputs

count_input()


