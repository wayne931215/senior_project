import numpy as np

dirr = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
SZ = 20

def bfs(maze):
    qx = [1]
    qy = [1]
    qz = [1]
    vis = np.zeros((SZ + 1, SZ + 1, SZ + 1))
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
            if tx < 1 or tx > SZ or ty < 1 or ty > SZ or tz < 1 or tz > SZ or vis[tx][ty][tz] or maze[tx][ty][tz] == 1:
                continue
            qx.append(tx)
            qy.append(ty)
            qz.append(tz)
            vis[tx][ty][tz] = 1
            dis[tx][ty][tz] = dis[x][y][z] + 1
    return dis[SZ][SZ][SZ]

print(bfs(np.random.randint(2, size=(SZ + 1, SZ + 1, SZ + 1))))
