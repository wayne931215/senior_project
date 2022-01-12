import numpy as np

dirr = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
SZ = 20
vis = np.zeros((3, SZ + 1, SZ + 1, SZ + 1))
maze = np.random.randint(2, size = (SZ + 1, SZ + 1, SZ + 1))

def walk(x, y, z, dx, dy, dz, id):
    cnt = 0
    while x <= SZ and y <= SZ and z <= SZ:
        if maze[x][y][z] == 1:
            break
        vis[id][x][y][z] = 1
        cnt += 1
        x += dx
        y += dy
        z += dz
    return cnt

def CountStraightRoute():
    res = 0
    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                if maze[i][j][k] == 1:
                    continue
                if i == 0 or maze[i - 1][j][k] == 1 and vis[0][i][j][k] == 0:
                    res += walk(i, j, k, 1, 0, 0, 0)
                if j == 0 or maze[i][j - 1][k] == 1 and vis[1][i][j][k] == 0:
                    res += walk(i, j, k, 0, 1, 0, 1)
                if k == 0 or maze[i][j][k - 1] == 1 and vis[2][i][j][k]:
                    res += walk(i, j, k, 0, 0, 1, 2)
    return res

print(CountStraightRoute())
