game_board = [
    ['','',''],
    ['','',''],
    ['','','']
]

# game_board[2][2] = 'x'


def showboard():
    print("------")
    for i in range(3):
        for j in range(3):
            print(f"|{game_board[i][j]}",end="")
        print("|",end="")
        print()
        print("------")

showboard()

selection = int(input("Which position do u want to choose(1-9 on the board): "))

if selection == 1:
    game_board[0][0]='X'

elif selection == 2:
    game_board[0][1]='X'


elif selection == 3:
    game_board[0][2]='X'



elif selection == 4:
    game_board[1][0]='X'



elif selection == 5:
    game_board[1][1]='X'



elif selection == 6:
    game_board[1][2]='X'



elif selection == 7:
    game_board[2][0]='X'


elif selection == 8:
    game_board[2][1]='X'


elif selection == 9:
    game_board[2][2]='X'

showboard()