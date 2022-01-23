import numpy as np
import var

dirr = var.dirr
SZ = var.SZ
Maze = np.zeros((SZ + 1, SZ + 1, SZ + 1))


def walk(x, y, z, dx, dy, dz):
    cnt = 0
    while x + dx <= SZ and y + dy <= SZ and z + dz <= SZ:
        if Maze[x][y][z] == 1:
            break
        cnt += 1
        x += dx
        y += dy
        z += dz

    return cnt


def count_straight_route(maze):
    res = 0
    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                Maze[i][j][k] = maze[i][j][k];

    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                if maze[i][j][k] == 1:
                    continue
                if i == 1 or maze[i - 1][j][k] == 1:
                    res += walk(i, j, k, 1, 0, 0)
                if j == 1 or maze[i][j - 1][k] == 1:
                    res += walk(i, j, k, 0, 1, 0)
                if k == 1 or maze[i][j][k - 1] == 1:
                    res += walk(i, j, k, 0, 0, 1)
    return res