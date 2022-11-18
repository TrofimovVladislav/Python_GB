# Регулярные выражения

# import re
# text = """100 ИНФ Информатика
# 213 МАТ Математика
# 156 АНГ Английский"""
# # извлечь все номера курсов
# ch = re.findall('[0-9]+', text)
# # извлечь все коды курсов (для латиницы [A-Z])
# codes = re.findall('[А-ЯЁ]{3}', text)
# # извлечь все названия курсов
# names = re.findall('[а-яА-ЯёЁ]{4,}', text)
# print (ch)
# print(codes)
# print(names)

#----------------------------------------------------------------------------------------

#Создайте программу для игры в "Крестики-нолики".


#----------------------------------------------------------------------------------------

# 1. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

# import re
# s = input('Введите: ')
# res=[]
# for i in s:
#     res.append(i)
# print(res)
 
# ert=[]  
# # we = [5, '+', 7, '-', 2, '*', 4, '-', 9, '/', 3]
# we = ['5', '+', '7', '-', '2', '*', '4', '-', '9', '/', '3']
# for i in range(len(we)-1):
#     if we[i]=='/':
#         ert = (''.join(we))
#         # sum = ('\d'/'\d')
#         print(ert)
    # if we[i]=='-':
    #    print(we[i-1]-we[i+1])
       
# match = re.search(r"_((\d+)_(\d+))_", your_string)

# print(match.group(1))  
# print(match.group(2))  
# print(match.group(3))  

# s = input('Введите: ')
# pattrn = ''
# res=[]
# for i, j in enumerate(s):
#     if s[i].isdigit():
#         res.append(int(j))
#     else:
#         res.append(j)
        
# print(res)

# import re
rer=[]
# # we = '5+7-2*4-9/3'
we = ['5', '+', '7', '-', '2', '*', '4', '-', '9', '/', '3']
for i in range(len(we)):
    if we[i].isdigit():
        rer.append(int(we[i]))
    else:
        rer.append(we[i])
for j in range(len(rer)):
    if rer[j]=='*':
        sum1 = str(rer[j-1]*rer[j+1])
        # print(rer[j-1:j+2])
        rer.replace((rer[j-1:j+2]) ,sum1)
        
        print(sum1)
        # rer.remove(rer[j])
    #     # sum = sum+1
    # if rer[j]=='/':
    #     sum2 = rer[j-1]-rer[j+1]
    #     print(rer[j-1:j+2])



# match = re.fullmatch(r'0-9', we)

# print(match.group())  
# # print(match.group(2))  
# # print(match.group(3))  

# from operator import __sub__, __add__
# from functools import reduce
# import re
# expr = '12-23+343+32'
# opf = {'+':__add__, '-':__sub__}
# vals = map(int, re.split('[+-]', expr))
# opl = filter(lambda x:x in '+-', expr)
# print(reduce(lambda x, y: opf[next(opl)](x, y), vals))


# expr = '12-23+343+322'
# def gv(expr):
#     v = ''
#     for c in reversed(expr):
#         v = c + v
#         if not c.isdigit():
#             yield int(v)
#             v = ''
#     yield int(v)
# print(sum(gv(expr)))


    

    
