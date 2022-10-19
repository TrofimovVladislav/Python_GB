# задача 2 . Задайте последовательность чисел.
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

num_list = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4]

def removing_duplicates(num_list):
    '''
    Функция удаляет дубликаты значений списка.
    '''
    list_not_duplicates = []
    
    for i in num_list:
        if i not in list_not_duplicates:
            list_not_duplicates.append(i)
    print(f'Последовательность с дубликатами:  {num_list} \nПоследовательность без дубликатов: {list_not_duplicates}')
    
    return list_not_duplicates
    
removing_duplicates(num_list)

