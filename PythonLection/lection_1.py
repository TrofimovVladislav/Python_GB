# print('hello world')
# типы данных и переменная
# int, float, boolean, str,list, None
# value = None
# print(type(value))


# a = 123
# b = 1.23
# print(type(a)) 
# print(type(b))

# value = None  если значение переменной пока не известно, можно объявить
# переменную со значением None, а потом вызвать переменную и присвоить ей нужное значение

# value = 12345 # например здесь 
# print(value)
# print(type(value))
# s = 'qwerty'
# s = 'qwerty "float" '
# s = 'qwerty \"sum'
# print(s)
# print(type(s))
# print(s)
# print(a, b, s)
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s)) # форматированный вывод
# print('{1} - {0} - {2}'.format(a, b, s)) # форматированный вывод
# print(f'{a} - {b} - {s}') # интерполяция
# f = True
# print(f)
# list = [1, 2, 3, 4, 5] # список (массив) чисел
# list = ['1', '2', '3', '4', '5', 'hello'] # список (массив) cnhjr
# print(list)

#Ввод и вывод данных
# print('Введите a')
# a = input()
# print('Введите b')
# b = input()

# print(a, ' + ', b, ' = ', a + b) # В данном случае будет произведено действие как сос трокой и результат будет сумма строк
# Чтобы складывались числа нужно использовать функцию int для перевода строки в число
# Для вещественных чисел используем float
# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())

# print(a, ' + ', b, ' = ', a+b)
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# Арифметические операции
# +, -, *, /, %, //, **
# **, +(унарный плюс), - (унарный минус), *, /, //, %, +, -
# (), Солращенные операции
# a = 8
# b = 3
# c = a + b # сложение
# c = a - b # вычитание
# c = a * b # умножение
# c = a / b # деление как для вещественных чисел
# c = a // b # деление в целых числах
# c = a % b # деление с остатком
# c = a ** b # возведение в степень
# print(c)

# a = 3
# b = 1.3123
# c = a * b
# c = round(a * b) # round - функция округления. 
# c = round(a * b, 5) # При добавлении аргумента, округление до определенного к-ва знаков
# print(c)

# Сокращенные операции присваивания
# a = 3
# a = a + 5
# a += 5 # Сокращенная форма присваивания
# print(a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 1 < 4 and 5 > 2 
# a = 1 == 2
# a = 1 != 2
# print(a)

# a = 'qwe'
# b = 'qwe'
# print(a == b)

# a = [1, 2]
# b = [1, 2]
# print(a == b)

# Тройное неравентсво

# a = 1 < 3 < 5
# print(a)

# func = 1
# T = 4
# x = 123

# print(func<T>x) 

# Логические операции

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1, 2, 3, 4, 5]
# print(f)
# print(2 in f)
# print( not 2 in f)

# f = [1, 2, 3, 4, 5]
# print(f)
# print(2 in f)
# print( not 2 in f)

# is_odd = f[0] % 2 == 0 # Определение четности. О - False, 1 - True
# is_odd = not f[0] % 2 # Другой способ определения четности, т.е остаток от деления не 1 (not 1), а это False 
# print(is_odd)

# Управляющие конструкции
# if, else, ifel,while, while else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это Маша')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original = original // 10 
#     # original //= 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original = original // 10 
#     # original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('Хватит')
# print(inverted)

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i**2)

# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(1, 5):
#     print(i)

# for i in range(1, 10, 2): # итерация с припащением 2
#     print(i)

# for i in 'qwerty':
#     print(i)

# text. - подсказка
# help(text.istitle) - пример вызова помощи

# text = 'съешь ущё этих мягких французских булок'
# print(len(text))                    # 39
# print('ещё' in text)                # True
# print(text.isdigit())               # False
# print(text.islower())               # True
# print(text.replace('ещё', 'ЕЩЁ'))   # 

# API для работы со строками - Срезы

# text = 'съешь ущё этих мягких французских булок'
# print(text[0])                  # с
# print(text[1])                  # ъ
# print(text[len(text)])          # IndexError
# print(text[len(text)] - 1)      # к
# print(text[-5])                 # б
# print(text[:])                  # print(text)
# print(text[:2])                  # съ
# print(text[len](text - 2:))     # ок
# print(text[2:9])                # ешь ещё
# print(text[6:-18])              # ещё этих мягких

# Списки

# numbers = [1, 2, 3, 4, 5]
# print(numbers)

# ran = range(1, 6)
# numbers = list(ran) # range изначально не является списком, поэтому его нужно привести к списку через list
# print(numbers) # [1, 2, 3, 4, 5]

# numbers[0] = 10
# print(f'{len(numbers)} len') # 5 len
# print(numbers)               # [10, 2, 3, 4, 5]

# for i in numbers:
#     i *= 2
#     print(i)                # [20, 4, 6, 8, 10]
# print(numbers)              # [10, 2, 3, 4, 5]


# добавление элемента append - добавить в конец
# remove - удаление элемента

# colors = ['red', 'green', 'blue']
# for e in colors:
#  print(e) # red green blue
# for e in colors:
#  print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

# Функции

# def f(x):
#     return x**2

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return
# arg = 1
# print(f(arg))
# print(type(f(arg)))

# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # NoneType


# Задача 5 Семинар 1
# Задача 5 VERY HARD SORT необязательная

# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается 
# с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10

# arr = [1, 4, 7, 2], [5, 9, 10, 3]
# print(arr)
# err_sor = sorted(arr[0] + arr[1])
# a = int((len(err_sor)/2))
# wer = err_sor[:a], err_sor[a:]
# print (wer)

# def chunks(n):
#     return [l[i:i+n] for i in range(0, len(l), n)]

# l = [1,2,3,4,5,6,7,8]
# while 1:
#     try:
#         # n = int(input('What size? '))
#         break
#     except ValueError:
#         print ('Numbers only please')

# print(chunks(int(len(l)/2)))

# size = int(input())
# array_input = []
# for x in range(size): 
#     array_input.append([int(y) for y in input().split()])
#     print(array_input)


# wer = [wer[0], wer[1]]
# def custom_key(people): 
#     return people[0] # second parameter denotes the age

# persons = [[1, 4, 7, 2], [5, 9, 10, 3]]
# print(f'Before sorting: {persons}') 
# persons.sort()
# print(f'After sorting: {persons}')


# def create_array():
#     size = int(input('Введите размер массива: '))
#     array_input = [] 
#     for x in range(size): 
#         array_input.append([int(y) for y in input('Введите элементы массива: ').split()]) 
#     print(array_input)
#     return(array_input)
    
# create_array()

# size = int(input('Введите размер: '))
# arr = int(input('Введите массив: '))
# array = []
# for x in range(size):
#     for y in arr:
#         array.append([int(arr)])
# print(array)

# 4. Выполнить алгоритм сортировки пузырьком
# Это решение без temp, но можно и с temp, потом обязательно сделай.
# list_numbers = [1, 8, 16, 3, 5, 9, 15, 1]
# n = len(list_numbers)
# for i in range(len(list_numbers) - 1):
#     for j in range(n - i - 1):
#         if list_numbers[j] > list_numbers[j + 1]:
#             list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]
# print(list_numbers)


# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
    
# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)

