def board():
    print("1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9")


def board_game(g):
    txt = ""
    ii = 1
    c = 0
    print()
    for _ in g:
        if i == 0:
            txt += " "
        elif i == 1:
            txt += "X"
        elif i == 2:
            txt += "O"
        elif ii % 3 == 0:
            if c <= 1:
                txt += "\n-+-+-\n"
                c += 1
        else:
            txt += "|"
        ii += 1

    print(txt)


def endgame(g):
    for _ in g:
        if i == 0:
            return False
    return True


def checkwin(g):
    if (g[0] == 1 and g[1] == 1 and g[2] == 1) or (g[0] == 2 and g[1] == 2 and g[2] == 2):
        board()
        board_game(g)
        if g[0] == 1 and g[1] == 1 and g[2] == 1:
            print("X wins.")
        else:
            print("O wins.")
        return True
    elif (g[3] == 1 and g[4] == 1 and g[5] == 1) or (g[3] == 2 and g[4] == 2 and g[5] == 2):
        board()
        board_game(g)
        if g[3] == 1 and g[4] == 1 and g[5] == 1:
            print("X wins.")
        else:
            print("O wins.")
        return True
    elif (g[6] == 1 and g[7] == 1 and g[8] == 1) or (g[6] == 2 and g[7] == 2 and g[8] == 2):
        board()
        board_game(g)
        if g[6] == 1 and g[7] == 1 and g[8] == 1:
            print("X wins.")
        else:
            print("O wins.")
        return True
    elif (g[0] == 1 and g[3] == 1 and g[6] == 1) or (g[0] == 2 and g[3] == 2 and g[6] == 2):
        board()
        board_game(g)
        if g[0] == 1 and g[3] == 1 and g[6] == 1:
            print("X wins.")
        else:
            print("O wins.")
        return True
    elif (g[1] == 1 and g[4] == 1 and g[7] == 1) or (g[1] == 2 and g[4] == 2 and g[7] == 2):
        board()
        board_game(g)
        if g[1] == 1 and g[4] == 1 and g[7] == 1:
            print("X wins.")
        else:
            print("O wins.")
        return True
    elif (g[2] == 1 and g[5] == 1 and g[8] == 1) or (g[2] == 2 and g[5] == 2 and g[8] == 2):
        board()
        board_game(g)
        if g[2] == 1 and g[5] == 1 and g[8] == 1:
            print("X wins.")
        else:
            print("O wins.")
        return True
    elif (g[0] == 1 and g[4] == 1 and g[8] == 1) or (g[0] == 2 and g[4] == 2 and g[8] == 2):
        board()
        board_game(g)
        if g[0] == 1 and g[4] == 1 and g[8] == 1:
            print("X wins.")
        else:
            print("O wins.")
        return True
    elif (g[2] == 1 and g[4] == 1 and g[6] == 1) or (g[2] == 2 and g[4] == 2 and g[6] == 2):
        board()
        board_game(g)
        if g[2] == 1 and g[4] == 1 and g[6] == 1:
            print("X wins.")
        else:
            print("O wins.")
        return True
    return False


print("Start Tic Tac Toe\n")
point = [0, 0, 0, 0, 0, 0, 0, 0, 0]
xo = ["X", "O"]
i = 0
while True:
    board()
    board_game(point)
    while True:
        pos = input("Input a number 1 to 9 to place " + xo[i] + " in one of the nine squares: ")
        try:
            pos = int(pos)
            if point[pos - 1] == 0:
                break
        except:
            pass
    if type(pos) is int:
        if 1 <= pos <= 9:
            if i == 0:
                i = 1
                point[pos - 1] = 1
            else:
                i = 0
                point[pos - 1] = 2
    if checkwin(point):
        break
    if endgame(point):
        board()
        board_game(point)
        print("Both tie.")
        break
