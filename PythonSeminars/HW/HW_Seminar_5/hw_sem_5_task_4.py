# задача 4 необязательная Даны два многочлена. 
# Задача - сформировать их сумму.

# например, 5*x^3 + 2*x^2 + 6 и 7*x^2 + 6*x + 3 , 
# Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9

# pol_1 = '5*x^3 + 14*x^2 + 6'
# pol_2 = '7*x^2 + 6*x + 3'



# print(pol_1 + pol_2)
# pol_0 = (pol_1 + pol_2)

# pol_3 = ''
# for i in pol_0:
#     print(i)
    # if 'x^2' in i:
    #     pol_3.append(i)
    #     print(pol_3)
        # pol_3.remove('*x^2')
        # print(pol_3)

# for i in pir_1:
#     if 'x^2' in i:
        
#         print(i[:])
#         sum = (int(i[:1]) + int(i[:1]))
        # print(sum)
        

    # if 'x^2' in i:
    #     print(pir_1[0])
# for j in pir_2:
#     if 'x^2' in j:
#         print(j)
        
# print(i[0])

# pol = '5*x^3 + 14*x^2 + 6 = 0'

import re
import itertools


file_1 = 'C:/GB/Python_GB/PythonSeminars/HW/HW_Seminar_5/33_Polynomial.txt'
file_2 = 'C:/GB/Python_GB/PythonSeminars/HW/HW_Seminar_5/33_Polynomial2.txt'
# file2 = '33_Polynomial2.txt'
file_sum = '34_Sum_polynomials.txt'

# Получение данных из файла

def read_pol(file):
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol

# Получение списка кортежей каждого (<коэффициент>, <степень>)

def convert_pol(pol):
    pol = pol.replace('= 0', '')
    pol = re.sub("[*|^| ]", " ", pol).split('+')
    pol = [char.split(' ') for char in pol]
    pol = [[x for x in list if x] for list in pol]
    for i in pol:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    pol = [tuple(int(x) for x in j if x != 'x') for j in pol]
    return pol

# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)

def fold_pols(pol1, pol2):   
    x = [0] * (max(pol1[0][1], pol2[0][1] + 1))
    for i in pol1 + pol2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    return res

# Составление итогового многочлена

def get_sum_pol(pol):
    var = ['*x^'] * len(pol)
    coefs = [x[0] for x in pol]
    degrees = [x[1] for x in pol]
    new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
    for x in new_pol:
        if x[0] == '0': del (x[0])
        if x[-1] == '0': del (x[-1], x[-1])
        if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
        if len(x) > 1 and x[-1] == '1': 
            del x[-1]
            x[-1] = '*x'
        x.append(' + ')
    new_pol = list(itertools.chain(*new_pol))
    new_pol[-1] = ' = 0'
    return "".join(map(str, new_pol))

def write_to_file(file, pol):
    with open(file, 'w') as data:
        data.write(pol)

pol1 = read_pol(file_1)
pol2 = read_pol(file_2)
pol_1 = convert_pol(pol1)
pol_2 = convert_pol(pol2)

pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
# print(pol_sum)
# write_to_file(file_sum, pol_sum)

print(pol1)
print(pol2)
print(pol_sum)