# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def floats_diff(float_list = []):
    '''
    Функция находит разницу между минимальной и 
    максимальной дробной частью значений элементов списка.
    '''
    float_min = 1
    float_max = 0
   
    for i in float_list:
        if (i - int(i)) < float_min:
            float_min = float("{0:.2f}".format(i - int(i)))
        if (i - int(i)) >= float_max:
            float_max = float("{0:.2f}".format(i - int(i)))
        result = float_max - float_min
    print(f'Разница максимальной ({float_max}) и минимальной ({float_min}) дробной части элементов списка = {float("{0:.2f}".format(result))}')

    return result
    
    
floats_diff([1.1, 1.2, 3.1, 5.17, 10.02])
floats_diff([4.07, 5.1, 8.2444, 6.98])