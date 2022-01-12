import numpy as np

dirr = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
SZ = 20
maze = np.random.randint(2, size = (SZ + 1, SZ + 1, SZ + 1))

def Proper(x, y, z):
    if x < 1 or x > SZ or y < 1 or y > SZ or z < 1 or z > SZ:
        return False
    elif maze[x][y][z] == 1:
        return False
    return True

def CountCrossroads():
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
                    if Proper(tx, ty, tz) == False:
                         continue
                    res += 1
    return res

print(CountCrossroads())
