# задача5 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , 
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. 
# Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно 
# переместился на другое место и выполнить это за m*n / 2 итераций. 
# То есть если массив три на четыре, то надо выполнить не более 6 итераций. 
# И далее в конце опять вывести на экран как таблицу.

# a = [2]
# for i in range(10):
#     a.append(i)
# print(a)

# a = 4
# mas = [] 
# for i in range(a): 
#     mas.append([0] * a)
# print(mas)

# a=int(input())
# mas = [] 
# for i in range(a): 
#     mas.append(list(map(int, input().split())))
# print(mas) 

# mas = [list(map(int, input().split())) for i in range(int(input()))]

#------------------------------------------------------
# Для обработки и вывода списков используются два вложенных цикла. 
# Первый цикл – по порядковому номеру строки, 
# второй – по ее элементам. Например, вывести массив можно так:

# mas = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

# for i in range(0, len(mas)):
#     for i2 in range(0, len(mas[i])):
#         print(mas[i], end=' ')
#     print()

# Выведет
# 1 1 1
# 1 1 1
# 1 1 1
#------------------------------------------------------
# То же самое можно сделать не по индексам, 
# а по значениям массива:

# mas = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# for i in mas: 
#     for i2 in i: 
#         print(i2, end=' ') 
#     print()

# Выведет
# 1 1 1
# 1 1 1
# 1 1 1
#------------------------------------------------------
# Способ с использованием метода join():

# mas = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# for i in mas: 
#     print(' '.join(list(map(str, i))))

# Выведет
# 1 1 1
# 1 1 1
# 1 1 1
#------------------------------------------------------

# Вывод одной из строк двумерного массива можно осуществить 
# с помощью цикла и того же метода join(). 
# Для примера выведем вторую строку в произвольном двумерном массиве:

# mas = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# string = 2
# for i in mas[string-1]:
#     print(i, end=' ')

# Выведет 1 1 1
#-------------------------------------------------------

# Для вывода определенного столбца в двумерном массиве 
# можно использовать такую программу:

# mas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# column = 2
# for i in mas:
#     print(i[column-1], end=' ')
# Выведет 2 5 8
#------------------------------------------------------

# Обработка двумерных массивов
# Составим произвольный двумерный массив с числами и размерностью 4x4:

# 2 4 7 3
# 4 5 6 9
# 1 0 4 2
# 7 8 4 7

# Теперь поставим числа в каждой строке по порядку:

# mas = [[2, 4, 7, 3], [4, 5, 6, 9], [1, 0, 4, 2], [7, 8, 4, 7]]
# mas2 = []
# for i in mas:
#     mas2.append(sorted(i))
# print(mas2)

# Выведет [[2, 3, 4, 7], [4, 5, 6, 9], [0, 1, 2, 4], [4, 7, 7, 8]]
#-------------------------------------------------------------------

# А теперь расставим все числа по порядку, 
# вне зависимости от их нахождения в определенной строке:

# mas = [[2, 4, 7, 3], [4, 5, 6, 9], [1, 0, 4, 2], [7, 8, 4, 7]]
# mas2 = []
# for i in mas:
#     for i2 in i:
#         mas2.append(i2)
# mas=sorted(mas2)
# for x in range(0, len(mas), 4):
#     e_c = mas[x : 4 + x]
#     if len(e_c) < 4:
#         e_c = e_c + [None for y in range(n - len(e_c))]
#     print(list(e_c))

# Выведет
# [0, 1, 2, 2]
# [3, 4, 4, 4]
# [4, 5, 6, 7]
# [7, 7, 8, 9]
#-----------------------------------------------------------------

size = int(input())
array_input = []
for x in range(size):
    array_input.append([int(y) for y in input().split()])
    print(array_input)