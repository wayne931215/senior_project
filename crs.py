import var
import random
import FitnessValue1 as f1
import numpy as np
import time

SZ = var.SZ
E = np.zeros((SZ + 1, SZ + 1))
maze = np.zeros((SZ + 1, SZ + 1, SZ + 1))
px = np.zeros((SZ + 1, SZ + 1), dtype = int)
py = np.zeros((SZ + 1, SZ + 1), dtype = int)
dirr = [[1, 0], [-1, 0], [0, 1], [0, -1]]
index = [0, 1, 2, 3]

def dfs(x, y, ex, ey):
    if x == ex and y == ey:
        return
    
    random.shuffle(dirr)

    for a, b in dirr:
        tx = x + a
        ty = y + b
        if tx < 1 or tx > SZ or ty < 1 or ty > SZ or px[tx][ty] != 0:
            continue

        px[tx][ty] = x
        py[tx][ty] = y
        dfs(tx, ty, ex, ey)


def crossover(maze1, maze2):
    random.seed(time.time())
    key = random.randint(2, SZ - 1)
    p = []
    q = []
    f1.count_distance(maze1, 1, 1, 1, 1, key - 1)
    for i in range (1, SZ + 1):
        for j in range(1, SZ + 1):
            if f1.dis[key - 1][i][j] != 0:
                p.append((i - 1) * SZ + j - 1)
    
    f1.count_distance(maze2, SZ, SZ, SZ, key + 1, SZ)
    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            if f1.dis[key + 1][i][j] != 0:
                q.append((i - 1) * SZ + j - 1)
    
    random.shuffle(p)
    random.shuffle(q)

    sx = p[0] // SZ + 1
    sy = p[0] % SZ + 1
    ex = q[0] // SZ + 1
    ey = q[0] % SZ + 1

    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            px[i][j] = 0
            py[i][j] = 0
            E[i][j] = 1
    
    E[sx][sy] = 0
    px[sx][sy] = sx
    py[sx][sy] = sy
    dfs(sx, sy, ex, ey)

    x = ex
    y = ey
    while x != sx or y != sy:
        E[x][y] = 0
        tmpx = px[x][y]
        y = py[x][y]
        x = tmpx
    
    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                if i < key:
                    maze[i][j][k] = maze1[i][j][k]
                elif i == key:
                    maze[i][j][k] = E[j][k]
                else:
                    maze[i][j][k] = maze2[i][j][k]

    if f1.count_distance(maze, 1, 1, 1, 1, SZ) == 0:
        print(sx, sy, ex, ey)
        for i in range(1, SZ + 1):
            for j in range(1, SZ + 1):
                print(E[i][j], end = ' ')
            print()
# crossover(np.zeros((SZ + 1, SZ + 1, SZ + 1)), np.zeros((SZ + 1, SZ + 1, SZ + 1)))