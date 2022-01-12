import numpy as np

dirr = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
SZ = 20

def cal(maze):
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
                    if tx < 1 or tx > SZ or ty < 1 or ty > SZ or tz < 1 or tz > SZ or maze[tx][ty][tz] == 1:
                         continue
                    res += 1
    return res

print(cal(np.random.randint(2, size = (SZ + 1, SZ + 1, SZ + 1))))
