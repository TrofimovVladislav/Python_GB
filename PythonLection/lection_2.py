# path = 'C:/GB/Python_GB/PythonLection/pytext.txt'

# with open(path, 'r') as file:
#     f = file.read().split()

# z = []
# def conv(f):
#     return [z.append(int(i)) for i in f] 
     

# res = [(i, i**2) for i in z if not i%2]
# print(res)


list1 = '1 2 3 5 6 14 38'.split()
# f = lambda x: x**2 
# list2 = [(i, f(i)) for i in list1 if i%2==0]
# print(list2)

def select(f, col):
    return [f(x) for x in col]
print(select(int, list1))

def wert(f, col):
    res = [lambda x: x not x%2]