# задача 5 необязательная Дан список чисел. 
# Создайте список, в который попадают числа, 
# описывающие максимальную возрастающую последовательность. 
# Порядок элементов менять нельзя.

# *Пример:*


# nums1 = [1, 5, 2, 3, 4, 6, 1, 7] #=> [1, 7]
# nums2 = [1, 5, 2, 3, 4, 1, 7]    #=> [1, 5]


def find_list(start_num, current_list):
    new_list = [start_num]
    max_num = max(current_list)

    for k in range(start_num, max_num):
        if start_num + 1 in current_list:
            new_list.append(start_num + 1)
            start_num += 1
                       
    if len(new_list) > 1:
        return new_list

    return []

list_of_numbers = [1, 5, 3, 2, 4, 1, 7]
lists = []
min_num = min(list_of_numbers)

current_list = find_list(min_num, list_of_numbers)
print(current_list)








# def max_sequence(seq):
#     temp = []
#     res = []
#     nums_max = max(seq)
#     nums_max_index = enumerate([nums_max])
#     for i, el in enumerate(seq):
#         if el == nums_max:
#             nums_max_index = i
#     for i in range(nums_max_index):
#         if seq[nums_max_index - i] < seq[nums_max_index]:
#             temp.append(seq[nums_max_index - i])
#             seq[nums_max_index] = seq[nums_max_index - i]
#     for j in reversed(temp):
#         res.append(j)
#     res.append(nums_max)
#     print(res)
#     return res

# max_sequence(nums1)
# max_sequence(nums2)