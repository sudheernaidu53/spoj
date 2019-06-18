global way
way = [[[0]*15 for i in range(15)] for j in range(15)] #0 or float(0) or numpy.int(0), numpy.float(0),numpy.longdouble(0)..
def beewalk(n):
    way[0][7][7]=1
    for i in range(1,n+1):
        for j in range(1,14):
            for k in range(1,14):
                way[i][j][k] = way[i-1][j][k+1]+way[i-1][j][k-1]+way[i-1][j+1][k]+way[i-1][j-1][k]+way[i-1][j+1][k-1]+way[i-1][j-1][k+1]
    return way[n][7][7]
T = int(input())
for i in range(T):
    print((beewalk(int(input()))))