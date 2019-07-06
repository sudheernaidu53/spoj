def greedyrooks(chessboard):
    for i in range(8):
        if (list(chessboard[i]).count('R') == 1):
            continue
        else:
            return False
        if (list(chessboard.T)[i].count('R') == 1):
            continue
        else:
            return False
    return True
T = int(input())
for i in range(T):
    chessboard = [[0]*8 for _ in range(8)]
#     for i in range(8):
    rawinput = (input().split())
    for j in range(len(rawinput)):
        chessboard[j] = list(rawinput(j))
    chessboard = numpy.array(chessboard)
    print(greedyrooks(chessboard))