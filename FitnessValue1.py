import numpy as np
import var

SZ = var.SZ
dirr = var.dirr
vis = np.zeros((SZ + 1, SZ + 1, SZ + 1))
dis = np.zeros((SZ + 1, SZ + 1, SZ + 1))

def count_distance(maze, sx, sy, sz, ub, db):
    qx = [sx]
    qy = [sy]
    qz = [sz]
    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                vis[i][j][k] = 0
                dis[i][j][k] = 0
                
    vis[sx][sy][sz] = 1
    dis[sx][sy][sz] = 1
    while qx:
        x = qx.pop(0)
        y = qy.pop(0)
        z = qz.pop(0)
        for a, b, c in dirr:
            tx = x + a
            ty = y + b
            tz = z + c
            if tx < ub or tx > db:
                continue
            if not var.proper(tx, ty, tz) or vis[tx][ty][tz] == 1 or maze[tx][ty][tz] == 1:
                continue
            qx.append(tx)
            qy.append(ty)
            qz.append(tz)
            vis[tx][ty][tz] = 1
            dis[tx][ty][tz] = dis[x][y][z] + 1
            
    return dis[SZ][SZ][SZ]

