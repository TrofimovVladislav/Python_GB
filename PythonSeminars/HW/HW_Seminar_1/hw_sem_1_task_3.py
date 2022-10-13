# задача 3. Напишите программу, которая принимает на вход 
# координаты точки (X и Y), и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def check_digit(msg):
    """
    Функция проверяет является ли введенное значение числом, 
    в том числе если оно отрицательное.
    """
    input_data = input(msg)
    try:
        int(input_data)
    except ValueError:
        print('\nВведенное значение не является числом.\nПовторите ввод.\n')
        return check_digit(msg)
    else:
        return input_data

def find_quarter():
    """
    Функция по введенным значениям координатам, выдает
    положение точки на плоскости координат.
    """
    coordinate_x = check_digit('\nВведите значение координаты X: ')
    coordinate_y = check_digit('Введите значение координаты Y: ')
    
    coordinate_x = int(coordinate_x)
    coordinate_y = int(coordinate_y)
    
    if coordinate_x > 0 and coordinate_y > 0:
        print('Точка в первой четверти.')
    elif coordinate_x < 0 and coordinate_y > 0:
        print('Точка во второй четверти.')
    elif coordinate_x < 0 and coordinate_y < 0:
        print('Точка в третьей четверти.')
    elif coordinate_x > 0 and coordinate_y < 0:
        print('Точка в четвертой четверти.')
    elif coordinate_x < 0 or coordinate_x > 0 and coordinate_y == 0:
        print('Точка находится на оси X.')
    elif coordinate_x == 0 and coordinate_y < 0 or coordinate_y > 0:
        print('Точка находится на оси Y.')
    elif coordinate_x == 0 and coordinate_y == 0:
        print('Точка на пересечении осей координат.')
         
find_quarter()

