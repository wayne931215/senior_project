import numpy as np
import var
import gen
import FitnessValue1 as f1
import FitnessValue2 as f2
import FitnessValue3 as f3
import sel
import crs
import mut

num = var.N
SZ = var.SZ
MAX = var.MAX
maze = np.zeros((num, SZ + 1, SZ + 1, SZ + 1))
Maze = np.zeros((num, SZ + 1, SZ + 1, SZ + 1))
fv = []

# generate initial maze and calculate their fitness value
for t in range(num):
    # generate initial maze
    gen.generate()

    for i in range(1, SZ + 1):
            for j in range(1, SZ + 1):
                for k in range(1, SZ + 1):
                    maze[t][i][j][k] = gen.maze[i][j][k]

    # calculate their fitness value
    v1 = f1.count_distance(maze[t], 1, 1, 1, 1, SZ)
    v2 = f2.count_crossroads(maze[t])
    v3 = MAX - f3.count_straight_route(maze[t])
    fv.append(v1 * 200 + v2 / 3 + v3)
    print(v1, v2, v3)

for generation in range(SZ):
    print(generation)
    for i in range(num):
        # select and crossover
        x = sel.select(num, fv)
        y = sel.select(num, fv)
        print(i, "select okay!")
        crs.crossover(maze[x], maze[y])
        print(i, "crossover okay!")
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                for l in range(1, SZ + 1):
                    Maze[i][j][k][l] = crs.maze[j][k][l]

    
    # repalce the original datas
    for i in range(num):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                for l in range(1, SZ + 1):
                    maze[i][j][k][l] = Maze[i][j][k][l]
"""
    # mutation
    for i in range(num):
        if mut.mutate(maze[i]) == True:
            maze[i][mut.kx][mut.ky][mut.kz] = 1

        v1 = f1.count_distance(maze[i], 1, 1, 1, 1, SZ)
        v2 = f2.count_crossroads(maze[i])
        v3 = MAX - f3.count_straight_route(maze[i])
        fv[i] = SZ * SZ * (SZ - 1) * 3 - v1 * 200 + v2 / 3 + v3
    print("finish mutation")
    
"""
maxx = fv[0]
index = 0

for i in range(1, num):
    if fv[i] > maxx:
        maxx = fv[i]
        index = i