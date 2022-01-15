import numpy as np
import var

SZ = var.SZ
dirr = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
vis = np.zeros((SZ + 1, SZ + 1, SZ + 1))


def proper(x, y, z):
    if x < 1 or x > SZ or y < 1 or y > SZ or z < 1 or z > SZ:
        return False
    elif vis[x][y][z] == 1:
        return False
    return True


def count_distance(maze):
    qx = [1]
    qy = [1]
    qz = [1]
    dis = np.zeros((SZ + 1, SZ + 1, SZ + 1))
    vis[1][1][1] = 1
    while qx:
        x = qx.pop(0)
        y = qy.pop(0)
        z = qz.pop(0)
        for a, b, c in dirr:
            tx = x + a
            ty = y + b
            tz = z + c
            if maze[tx][ty][tz] == 1 or not proper(tx, ty, tz):
                continue
            qx.append(tx)
            qy.append(ty)
            qz.append(tz)
            vis[tx][ty][tz] = 1
            dis[tx][ty][tz] = dis[x][y][z] + 1
    return dis[SZ][SZ][SZ]

