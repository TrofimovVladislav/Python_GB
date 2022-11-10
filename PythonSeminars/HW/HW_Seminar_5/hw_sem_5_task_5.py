# задача 5 необязательная Дан список чисел. 
# Создайте список, в который попадают числа, 
# описывающие максимальную возрастающую последовательность. 
# Порядок элементов менять нельзя.

# *Пример:*
#  
nums1 = [1, 5, 2, 3, 4, 6, 1, 7] #=> [1,  7] 
nums2 = [1, 5, 2, 3, 4, 1, 7, 8, 15, 1, 3, 6] #=> [1,  5] ?????????
nums3 = [1, 5, 2, 3, 4, 6, 1, 3, 5, 7, 9, 11, 15, 2, 4, 9] #=> [1, ,3, 5, 7, 9, 11, 15]

def max_sequence(seq):
    temp = []
    res = []
    nums_max = max(seq)
    nums_max_index = enumerate([nums_max])
    for i, el in enumerate(seq):
        if el == nums_max:
            nums_max_index = i
    for i in range(nums_max_index):
        if seq[nums_max_index - i] < seq[nums_max_index]:
            temp.append(seq[nums_max_index - i])
            seq[nums_max_index] = seq[nums_max_index - i]
    for j in reversed(temp):
        res.append(j)
    res.append(nums_max)
    print(res)
    return res

max_sequence(nums1)
max_sequence(nums2)
max_sequence(nums3)

nums_max = max(nums1)
nums_max_index = lambda i, e: enumerate([nums_max]): if el == nums_max 