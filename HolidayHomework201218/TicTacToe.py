# 3. Направете игра на морски шах. Ходовете трябва да взимате от input. Ходовете може да ги записванете в двумерен списък, като може и да не чертаете игралното поле.

import os

def print_board(game_array):
    os.system('cls' if os.name=='nt' else 'clear')
    print(f'     |     |')
    print(f'  {game_array[0][0]}  |  {game_array[0][1]}  |  {game_array[0][2]}')
    print(f'     |     |')
    print('-----------------')
    print(f'     |     |')
    print(f'  {game_array[1][0]}  |  {game_array[1][1]}  |  {game_array[1][2]}')
    print(f'     |     |')
    print('-----------------')
    print(f'     |     |')
    print(f'  {game_array[2][0]}  |  {game_array[2][1]}  |  {game_array[2][2]}')
    print(f'     |     |')

def has_won(game_array):
    if game_array[0][0] != ' ' and (game_array[0][0] == game_array[0][1] == game_array [0][2]):
        return True
    if game_array[1][0] != ' ' and (game_array[1][0] == game_array[1][1] == game_array [1][2]):
        return True
    if game_array[2][0] != ' ' and (game_array[2][0] == game_array[2][1] == game_array [2][2]):
        return True
    if game_array[0][0] != ' ' and (game_array[0][0] == game_array[1][0] == game_array [2][0]):
        return True
    if game_array[0][1] != ' ' and (game_array[0][1] == game_array[1][1] == game_array [2][1]):
        return True
    if game_array[0][2] != ' ' and (game_array[0][2] == game_array[1][2] == game_array [2][2]):
        return True
    if game_array[0][0] != ' ' and (game_array[0][0] == game_array[1][1] == game_array [2][2]):
        return True
    if game_array[0][2] != ' ' and (game_array[0][2] == game_array[1][1] == game_array [2][0]):
        return True
    return False

def has_draw(game_array):
    count = 0
    for i in range(3):
        for j in range(3):
            if game_array[i][j] != ' ':
                count += 1
    if count == 9:
        return True


game_array = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


while True:
    while True:
        p1x, p1y = map(int, input("Player1 on move: ").split())
        if p1x < 0 or p1x > 3 or p1y < 0 or p1y > 3:
            print("Invalit input.")
        elif game_array[p1x - 1][p1y - 1] != ' ':
            print("Filled space.")
        else:
            break
    game_array[p1x - 1][p1y - 1] = 'x'
    print_board(game_array)
    if has_won(game_array):
        print ("Player1 won!")
        break
    if has_draw(game_array):
        print ("Draw!")
        break
    while True:
        p2x, p2y = map(int, input("Player2 on move: ").split())
        if p2x < 0 or p2x > 3 or p2y < 0 or p2y > 3:
            print("Invalit input.")
        elif game_array[p2x - 1][p2y - 1] != ' ':
            print("Filled space.")
        else:
            break
    game_array[p2x - 1][p2y - 1] = 'o'
    print_board(game_array)
    if has_won(game_array):
        print ("Player2 won!")
        break
    if has_draw(game_array):
        print ("Draw!")
        break
print ("Thank you for playing!")