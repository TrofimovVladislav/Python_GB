path = 'C:/GB/Python_GB/PythonLection/pytext.txt'

with open(path, 'r') as f:
    data = f.read().split()
    
def select(f, col):
    return [f(x) for x in col]

def otbor(f, col):
    return [x for x in col if f(x)]

nums = select(int, data)
nums_chet = otbor(lambda x: not x % 2, nums)
res = select(lambda x: (x, x**2), nums_chet)

print(res)

exit()
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