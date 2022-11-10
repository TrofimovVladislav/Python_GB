# задача 3. Напишите программу, удаляющую из текста все слова, 
# содержащие "абв". 
# Функции FIND и COUNT юзать нельзя.

str_in = 'Забвение на сабвее никогда не сабвуфер и не забава.'

def sort_str(string):
    str_sorted = str_in.split()
    list = [str_sorted.remove(i) for i in str_sorted if 'абв' in i]
    print(' '.join(str_sorted))

sort_str(str_in)


