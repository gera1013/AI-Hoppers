from board import print_board
from alpha_beta import Game

board = [
    #0 #1 #2 #3 #4 #5 #6 #7 #8 #9
    [2, 2, 2, 2, 2, 0, 0, 0, 0, 0], #0
    [2, 2, 2, 2, 0, 0, 0, 0, 0, 0], #1
    [2, 2, 2, 0, 0, 0, 0, 0, 0, 0], #2
    [2, 2, 0, 0, 0, 0, 0, 0, 0, 0], #3
    [2, 0, 0, 0, 0, 0, 0, 0, 0, 0], #4
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #5
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #6
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], #7
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1], #8
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 1], #9
]

test_game = Game(board)
test_game.player = 2

alpha = Game(board)
alpha.player = 1


single = int(input("1. Jugador vs AI\n2. AI vs AI\n"))

print("START")
print_board(board)

if single == 1:
    print("Comienza en la posición arriba izquierda")
    print("Primer turno jugador")
    while True:
        ##Players move
        xi = int(input("INGRESE X INIT: "))
        yi = int(input("INGRESE Y INIT: "))
        xf = int(input("INGRESE X FINAL: "))
        yf = int(input("INGRESE Y FINAL: "))
        board[xi - 1][yi - 1] = 0
        board[xf - 1][yf - 1] = 2
        
        print("\nMOVE PLAYER", "(", xi, ",", yi, ")", ", (", xf, ",", yf, ")\n")
        print_board(board)

        if test_game.is_terminal(board, 2):
            print("PLAYER WINS!!")
            break

        print("\nCalculating...")
        pick = alpha.alpha_beta_pruning()

        board[pick[0][0]][pick[0][1]] = 0
        board[pick[1][0]][pick[1][1]] = 1

        print("\nMOVE MINIMAX", "(", pick[0][0], ",", pick[0][1], ")", ", (", pick[1][0], ",", pick[1][1], ")\n")
        print_board(board)
        if test_game.is_terminal(board, 1):
            print("MINIMAX WINS!!")
            break

if single == 2:
    while True:
        print("\nCalculating...")
        pick = test_game.alpha_beta_pruning()

        board[pick[0][0]][pick[0][1]] = 0
        board[pick[1][0]][pick[1][1]] = 2

        print("\nMOVE MINIMAX 1", "(", pick[0][0], ",", pick[0][1], ")", ", (", pick[1][0], ",", pick[1][1], ")\n")
        print_board(board)

        if test_game.is_terminal(board, 2):
            print("MINIMAX WINS!!")
            break
        
        print("\nCalculating...")
        pick = alpha.alpha_beta_pruning()

        board[pick[0][0]][pick[0][1]] = 0
        board[pick[1][0]][pick[1][1]] = 1

        print("\nMOVE MINIMAX 2", "(", pick[0][0], ",", pick[0][1], ")", ", (", pick[1][0], ",", pick[1][1], ")\n")
        print_board(board)
        if test_game.is_terminal(board, 1):
            print("PLAYER WINS!!")
            break