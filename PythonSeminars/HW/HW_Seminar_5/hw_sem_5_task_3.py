# задача 3. Напишите программу, удаляющую из текста все слова, 
# содержащие "абв". 
# Функции FIND и COUNT юзать нельзя.

ter = 'Забвение никогда не забава и не швабра'

ert = ter.split()
# list = [ert.remove(i) for i in ert if 'абв' in i]
list = [ert.remove(i) for i in ert if 'а' and 'б' and 'в' in i]
print(' '.join(ert))

# for i in ert:
#     # if 'а' and 'б' and 'в' in i:
#     if 'абв' in i:
#         ert.remove(i)
# print(' '.join(ert))



