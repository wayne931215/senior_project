import var
import random

SZ = var.SZ
dirr = var.dirr
kx = 0
ky = 0
kz = 0

def mutate(maze):
    x = []
    y = []
    z = []
    length = 0
    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                if i == SZ and j == SZ and k == SZ:
                    continue

                if maze[i][j][k] == 1:
                    x.append(i)
                    y.append(j)
                    z.append(k)
                    continue
                    
                cnt = 0
                for a, b, c in dirr:
                    tx = i + a
                    ty = j + b
                    tz = k + c
                    if var.proper(tx, ty, tz) and maze[tx][ty][tz] == 1:
                        cnt += 1
                
                if cnt == 1:
                    x.append(i)
                    y.append(j)
                    z.append(k)
                    length += 1
    if length == 0:
        return False

    key = random.randint(0, length - 1)
    kx = x[key]
    ky = y[key]
    kz = z[key]
    
    return True
