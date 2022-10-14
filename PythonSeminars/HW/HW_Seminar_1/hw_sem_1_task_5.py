# Задача 5 VERY HARD SORT необязательная

# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается 
# с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10

arr = [1, 4, 7, 2], [5, 9, 10, 3]
print(arr)
err_sor = sorted(arr[0] + arr[1])
a = int((len(err_sor)/2))
wer = err_sor[:a], err_sor[a:]
print (wer)

def chunks(n):
    return [l[i:i+n] for i in range(0, len(l), n)]

l = [1,2,3,4,5,6,7,8]
while 1:
    try:
        # n = int(input('What size? '))
        break
    except ValueError:
        print ('Numbers only please')

print(chunks(int(len(l)/2)))

size = int(input())
array_input = []
for x in range(size): 
    array_input.append([int(y) for y in input().split()])
    print(array_input)


# print(func)
# print(func)

# wer = [wer[0], wer[1]]
# def custom_key(people): 
#     return people[0] # second parameter denotes the age

# persons = [[1, 4, 7, 2], [5, 9, 10, 3]]
# print(f'Before sorting: {persons}') 
# persons.sort() 
# print(f'After sorting: {persons}')



# size = int(input())
# array_input = [] 
# for x in range(size): 
#     array_input.append([int(y) for y in input().split()]) 
# print(array_input)

# http://cs.mipt.ru/algo_fefm/lessons/lab6.html#section-3

# 4. Выполнить алгоритм сортировки пузырьком
# Это решение без temp, но можно и с temp, потом обязательно сделай.
# list_numbers = [1, 8, 16, 3, 5, 9, 15, 1]
# n = len(list_numbers)
# for i in range(len(list_numbers) - 1):
#     for j in range(n - i - 1):
#         if list_numbers[j] > list_numbers[j + 1]:
#             list_numbers[j], list_numbers[j + 1] = list_numbers[j + 1], list_numbers[j]
# print(list_numbers)


