# Задача 1 Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов 
# списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def sum_odd_index_numbers():
    '''
    Функция находит сумму элементов, стоящих на нечетных позициях списка.
    '''
    nums_quantity = int(input('Введите количество элементов списка: '))
    numbers_list = [randint(1, 100) for i in range(nums_quantity)]
    print(f'\nСписок чисел: {numbers_list}')
    sum_num = 0
    odd_list = []
    for i in range(1,len(numbers_list),2):
        sum_num = sum_num + numbers_list[i]
        odd_list.append(numbers_list[i])
    print(f'На нечетных позициях элементы {odd_list}, их сумма равна {sum_num}.\n')
    return sum_num
          
sum_odd_index_numbers()