import numpy as np
import var

SZ = var.SZ
dirr = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
vis = np.zeros((SZ + 1, SZ + 1, SZ + 1))


def count_distance(maze):
    qx = [1]
    qy = [1]
    qz = [1]
    dis = np.zeros((SZ + 1, SZ + 1, SZ + 1))
    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                vis[i][j][k] = 0
                
    vis[1][1][1] = 1
    while qx:
        x = qx.pop(0)
        y = qy.pop(0)
        z = qz.pop(0)
        for a, b, c in dirr:
            tx = x + a
            ty = y + b
            tz = z + c
            if not var.proper(tx, ty, tz) or vis[tx][ty][tz] == 1 or maze[tx][ty][tz] == 1:
                continue
            qx.append(tx)
            qy.append(ty)
            qz.append(tz)
            vis[tx][ty][tz] = 1
            dis[tx][ty][tz] = dis[x][y][z] + 1
    return dis[SZ][SZ][SZ]

