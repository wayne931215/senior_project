import var
import random

SZ = var.SZ
dirr = var.dirr

def mutate(maze):
    x = []
    y = []
    z = []
    length = 0
    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                if maze[i][j][k] == 1:
                    continue
                cnt = 0
                for a, b, c in dirr:
                    tx = i + a
                    ty = j + b
                    tz = k + c
                    if proper(tx, ty, tz) and maze[tx][ty][tz] == 1:
                        cnt += 1
                
                if cnt == 1:
                    x.append(tx)
                    y.append(ty)
                    z.append(tz)
                    length += 1

    key = random.randint(0, length)
    kx = x[key]
    ky = y[key]
    kz = z[key]