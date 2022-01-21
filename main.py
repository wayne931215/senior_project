import gen
import FitnessValue1 as f1
import FitnessValue2 as f2
import FitnessValue3 as f3
import sel
import numpy as np
import var

num = 20
SZ = var.SZ
maze = np.zeros((num, SZ + 1, SZ + 1, SZ + 1))
Maze = np.zeros((num, SZ + 1, SZ + 1, SZ + 1))
value1 = []
value2 = []
value3 = []
tmp1 = []
tmp2 = []
tmp3 = []

# generate initial maze and calculate their fitness value
for t in range(num):
    # generate initial maze
    while 1:
        gen.generate()
        if f1.count_distance(gen.maze) != 0:
            break

    for i in range(1, SZ + 1):
            for j in range(1, SZ + 1):
                for k in range(1, SZ + 1):
                    maze[t][i][j][k] = gen.maze[i][j][k]

    # calculate their fitness value
    value1.append(f1.count_distance(maze[t]))
    value2.append(f2.count_crossroads(maze[t]))
    value3.append(f3.count_straight_route(maze[t]))
    print(value1[t], value2[t], value3[t])

"""
for generation in range(SZ):
    for i in range(num):
        # select and crossover
        x = sel.select(num, value1, value2, value3)
        y = sel.select(num, value1, value2, value3)
        crs.crossover(maze[x], maze[y])
        # calculate the fitness values
        tmp1.append(f1.count_distance(crs.res))
        tmp2.append(f2.count_crossroads(crs.res))
        tmp3.append(f3.count_straight_route(crs.res))
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                for l in range(1, SZ + 1):
                    Maze[i][j][k][l] = crs.res[j][k][l]


    # repalce the original datas
    for i in range(n):
        value1[i] = tmp1[i]
        value2[i] = tmp2[i]
        value3[i] = tmp3[i]
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                for l in range(1, SZ + 1):
                    maze[i][j][k][l] = Maze[i][j][k][l]

    # mutation
    tmp1.clear()
    tmp2.clear()
    tmp3.clear()
"""