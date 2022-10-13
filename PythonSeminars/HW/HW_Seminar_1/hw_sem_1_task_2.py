# задача 2. Напишите программу для проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def logical_statement():
    """
    Функция проверяет истинность логического утверждения.
    """
    
    for x in range(2):
        for y in range(2):
            for z in range(2):
                result = print((not (x or y or z) == (not x and not y and not z)), end=' ')
                print(x, y, z, end=' \n')
    if result == False:
        print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ложно.')
    else:
        print('\nУтверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истино.', '\n')

    return


logical_statement()