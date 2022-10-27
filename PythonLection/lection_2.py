path = 'C:/GB/Python_GB/PythonLection/pytext.txt'

with open(path, 'r') as file:
    fit = file.read().split()
    
rt = []
def lis_int(f, col):
    for x in col:
        rt.append(f(x))
    return rt
lis_int(int, fit)

res = []
def sqw(col):
    for x in col:
        if not x % 2:
            res.append((x, x**2))
    print(res)
    return res
sqw(rt)
    
    
# res = [(i, i**2) for i in z if not i%2]
# print(res)


# # list1 = '1 2 3 5 6 15 38'
# # list2 = list1.split()

# # def select(f, col):
# #     return [f(x) for x in col]
# # print(select(int, list2))

# # def chet(f, col):
# #     return [x for x in col if f(x)]

# # res = chet(lambda x: not x % 2, list2)

# # print(res)

# from datetime import date


# list_in = '1 2 3 5 6 15 38'
# list_conv_list = list_in.split()

# def str_to_int(f, col):
#     for i in col:
#         i = f(i)
#         print(i)
#     return i

# str_to_int(int, list_conv_list)