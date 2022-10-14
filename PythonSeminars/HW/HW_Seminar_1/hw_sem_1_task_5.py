# Задача 5 VERY HARD SORT необязательная
# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается 
# с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3
# После сортировки
# 1 2 3 4
# 5 7 9 10

def create_array():
    size = int(input('Введите размер массива: '))
    array_input = [] 
    for x in range(size): 
        array_input.append([int(y) for y in input('Введите элементы массива через пробел: ').split()]) 
    print(f'Исходный массив: {array_input}')
    return array_input

def sorted_2D_array():
    array = create_array()
    array_sorted = sorted(array[0] + array[1])
    len_ = int((len(array_sorted)/2))
    output_array = array_sorted[:len_], array_sorted[len_:]
    print (f'Отсортированный массив: {output_array}\n')
    return output_array

sorted_2D_array()