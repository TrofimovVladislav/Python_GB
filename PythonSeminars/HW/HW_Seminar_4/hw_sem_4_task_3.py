# задача 3. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл 
# многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

def polynom_random_coeff(k, min_val, max_val):
    '''
    Функция по заданной степени создает многочлен
    с рандомным списком коэффициентов.
    '''
    # k = 2 # Степень полинома
    coeff = []; coeff_no_zero = []; coeff_list = []
    
    for i in range(k):
        coeff.append(randint(min_val, max_val))
        if coeff[i] != 0:
            coeff_no_zero.append(coeff[i])
        k = len(coeff_no_zero)
        i = i + 1    
    for j in range(k):
        coeff_list.append(f'{coeff_no_zero[j]}x^{k}')
        k = k-1

    coeff_1 = randint(min_val, max_val) # Коэффициент без переменной
    if coeff_1 == 0: coeff_1 = ''
    polynom = f'{" + ".join(coeff_list)}' ' + ' f'{coeff_1}  = 0'
    '''
    Список замен при выводе в терминал
    '''
    polynom = polynom.replace(' +  ', '') 
    polynom = polynom.replace('x^1', 'x')
    polynom = polynom.replace('1x', 'x')
    polynom = polynom.replace('1x', 'x')
    # polynom = polynom.replace('0x', '')
    polynom_str = []
    polynom_str.append(polynom)
    # Запись многочлена в файл
    with open('polinoms.txt', 'a', encoding = 'UTF-8') as file:
        file.write(f'{polynom}\n')

    return polynom

print(polynom_random_coeff(2, 0, 100))
print(polynom_random_coeff(2, 0, 100))
print(polynom_random_coeff(2, 0, 100))
print(polynom_random_coeff(2, 0, 100))
print(polynom_random_coeff(2, 0, 100))






    




    

        
