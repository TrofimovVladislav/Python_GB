# Задача 2. Напишите программу, которая принимает на 
# вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def find_factorial(factorial_number):
    """
    Функция находит произведения чисел от 1 до N
    и выводит эти произведения в виде списка.
    """
    factorial_list = []
    # factorial_number = int(input('Число N: '))
    factorial_result = 1
    for i in range(factorial_number):
        factorial_result *= (i + 1)
        factorial_list.insert(i, factorial_result)
    print(f'\nНабор произведений чисел от 1 до {factorial_number}: {factorial_list}\n')
    
    return factorial_list


find_factorial(4)