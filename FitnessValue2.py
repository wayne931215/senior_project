import numpy as np
import var

dirr = var.dirr
SZ = var.SZ
maze = np.random.randint(2, size=(SZ + 1, SZ + 1, SZ + 1))


def count_crossroads(maze):
    res = 0
    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                if maze[i][j][k] == 1:
                    continue
                for a, b, c in dirr:
                    tx = i + a
                    ty = j + b
                    tz = k + c
                    if not var.proper(tx, ty, tz) or maze[tx][ty][tz] == 1:
                        continue
                    res += 1
    return res

