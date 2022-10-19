# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


def product_paired_elements():
    '''
    Функция находит произведение парных элементов списка.
    Первый * Последний, Второй * Предпоследний, и т.д. 
    '''
    nums_quantity = int(input('\nВведите количество элементов списка: '))
    numbers_list = [randint(1, 10) for i in range(nums_quantity)]
    print(f'Список чисел: {numbers_list}')
    output_list = []
    for i in range((len(numbers_list) + 1)//2):
        output_list.append(numbers_list[i] * numbers_list[len(numbers_list) - 1 - i])
    print(f'Список произведений парных элементов списка: {output_list}\n')

    return output_list

product_paired_elements()