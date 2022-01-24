import random
import var
import time
import numpy as np
import FitnessValue1 as f1
import FitnessValue2 as f2
import FitnessValue3 as f3


rate = var.arate
SZ = var.SZ
maze = np.ones((SZ + 1, SZ + 1, SZ + 1), dtype = int)
px = np.zeros((SZ + 1, SZ + 1, SZ + 1), dtype = int)
py = np.zeros((SZ + 1, SZ + 1, SZ + 1), dtype = int)
pz = np.zeros((SZ + 1, SZ + 1, SZ + 1), dtype = int)
dirr = var.dirr


def dfs():
    sx = [1]
    sy = [1]
    sz = [1]
    
    while sx:
        x = sx.pop()
        y = sy.pop()
        z = sz.pop()
        if x == SZ and y == SZ and z == SZ:
            break

        random.shuffle(dirr)
        for a, b, c in dirr:
            tx = x + a
            ty = y + b
            tz = z + c
            if not var.proper(tx, ty, tz) or px[tx][ty][tz] != 0:
                continue

            px[tx][ty][tz] = x
            py[tx][ty][tz] = y
            pz[tx][ty][tz] = z
            sx.append(tx)
            sy.append(ty)
            sz.append(tz)



def generate():

    random.seed(time.time())
    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                    px[i][j][k] = 0
                    py[i][j][k] = 0
                    pz[i][j][k] = 0
                    maze[i][j][k] = 1
    
    px[1][1][1] = 1
    py[1][1][1] = 1
    pz[1][1][1] = 1
    maze[1][1][1] = 0

    dfs()
    x = SZ
    y = SZ
    z = SZ
    cnt = 0
    while x != 1 or y != 1 or z != 1:
        maze[x][y][z] = 0
        tmpx = px[x][y][z]
        tmpy = py[x][y][z]
        z = pz[x][y][z]
        x = tmpx
        y = tmpy
        cnt += 1

    left = SZ * SZ * SZ * rate - cnt
    if left < 0:
        retuen
        
    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                if maze[i][j][k] == 1:
                    rd = random.randint(0, SZ * SZ * SZ - 1)
                    if rd < left:
                        maze[i][j][k] = 0
