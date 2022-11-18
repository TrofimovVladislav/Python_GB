
# board = range(1, 10)
# def draw_board(x):

#     print ("-------------------")
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ("-------------")
        
# draw_board(board)

maps = []
for i in range(1, 10):
    maps.append(i)

def draw_board(x):

    print ("-------------")
    for i in range(3):
        print ("|", maps[0+i*3], "|", maps[1+i*3], "|", maps[2+i*3], "|")
        print ("-------------")
  
def inp_():
    s = (int(input('Где крестик?: ')) - 1)
    if maps[s] != 'X':
        maps[s] = 'X'
    elif maps[s] == 'X':
        print('Ход не возможен. Переходи.')
        return inp_()
    if (maps.count('X') + maps.count('O')) < (len(maps)):
        draw_board(maps)
        return inp_()   
    else:
        return print('Все, Приехали )))')

draw_board(maps)
inp_()


# ret = []
# for i in range(1,10):
#     ret.append(i)
# print(ret)

# def inp_():
#     s = (int(input('Где крестик?: ')) - 1)
#     if ret[s] != 'X':
#         ret[s] = 'X'
#         print(board)
#     if ret.count('X') < (len(ret)):
#         return inp_()   
#     else:
#         return print('Все, Приехали )))')
# inp_()

#----------------------------------------------------------------------------------------

# # Инициализация карты
# maps = [1,2,3,
#         4,5,6,
#         7,8,9]

# # Инициализация победных линий
# victories = [[0,1,2],
#              [3,4,5],
#              [6,7,8],
#              [0,3,6],
#              [1,4,7],
#              [2,5,8],
#              [0,4,8],
#              [2,4,6]]
 
# # Вывод карты на экран
# def print_maps():
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])
 
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
 
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8])    
 
# # Сделать ход в ячейку
# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
 
# # Получить текущий результат игры
# def get_result():
#     win = ""
 
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"   
             
#     return win

# for i in victories:
#     print(maps[i[0]])


# # Основная программа
# game_over = False
# player1 = True
 
# while game_over == False:
 
#     # 1. Показываем карту
#     print_maps()
 
#     # 2. Спросим у играющего куда делать ход
#     if player1 == True:
#         symbol = "X"
#         step = int(input("Человек 1, ваш ход: "))
#     else:
#         symbol = "O"
#         step = int(input("Человек 2, ваш ход: "))
 
#     step_maps(step,symbol) # делаем ход в указанную ячейку
#     win = get_result() # определим победителя
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
 
#     player1 = not(player1)        
 
# # Игра окончена. Покажем карту. Объявим победителя.        
# print_maps()
# print("Победил", win)

#----------------------------------------------------------------------------------------


# board = range(1,10)

# #Теперь напишем функцию, которая будет выводить наше поле в привычном формате.

# def draw_board(board):
#     print ('------------')
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ('-------------')

# #Самое время дать пользователям возможность вводить данные в нашу игру. Пишем функцию take_input

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = raw_input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print "Некорректный ввод. Вы уверены, что ввели число?"
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print "Эта клеточка уже занята"
#         else:
#             print "Некорректный ввод. Введите число от 1 до 9 чтобы походить."

# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# #Осталось создать функцию main, в которой мы соберем вместе все описанные функции.

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print tmp, "выиграл!"
#                 win = True
#                 break
#         if counter == 9:
#             print "Ничья!"
#             break
#     draw_board(board)


print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")