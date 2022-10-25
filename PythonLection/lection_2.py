list2 = [1, 2, 3, 5, 6, 14, 38]
f = lambda x: x**2 
list1= [(i, f(i)) for i in list2 if i%2==0]
print(list1)