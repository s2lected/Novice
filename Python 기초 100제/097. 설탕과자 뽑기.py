h, w = input().split()
h = int(h)
w = int(w)

board = []

for i in range(h+1):
    board.append([])
    for j in range(w+1):
      board[i].append(0)

num = int(input())

for i in range(num):
    l, d, x, y = input().split()
    l = int(l)
    d = int(d)
    x = int(x)
    y = int(y)
    for j in range(l):
        if d == 0: board[x][y+j] = 1
        else: board[x+j][y] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        print(board[i][j],end=" ")
    print()
