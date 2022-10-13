# задача 4 HARD необязательная Напишите простой калькулятор, 
# который считывает с пользовательского ввода три строки: 
# первое число, второе число и операцию, после чего применяет 
# операцию к введённым числам ("первое число" "операция" "второе число") 
# и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div.

def calc():
    """
    Функция "Простой калькуолятор"
    """
    print('Введите данные для вычисления:')
    num_1 = int(input())
    num_2 = int(input())
    oper = str(input())
   
    result = 0
    if str(oper) == '+':
        result = num_1 + num_2
        print(f'Результат {result}')
    elif str(oper) == '-':
        result = num_1 - num_2
        print(f'Результат {result}')
    elif str(oper) == '*':
        result = num_1 * num_2
        print(f'Результат {result}')
    elif str(oper) == 'pow':
        result = num_1 ** num_2
        print(f'Результат {result}')
    elif str(oper) == 'mod':
        result = num_1 % num_2
        print(f'Результат {result}')
    elif str(oper) == '/' and num_2 != 0:
        result = num_1 / num_2
        print(f'Результат {result}')
    else: print('Деление на 0!')
        
calc()



