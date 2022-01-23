import gen
import FitnessValue1 as f1
import FitnessValue2 as f2
import FitnessValue3 as f3
import sel
import numpy as np
import var
import mut

num = var.N
SZ = var.SZ
maze = np.zeros((num, SZ + 1, SZ + 1, SZ + 1))
Maze = np.zeros((num, SZ + 1, SZ + 1, SZ + 1))
value1 = []
value2 = []
value3 = []

# generate initial maze and calculate their fitness value
for t in range(num):
    # generate initial maze
    gen.generate()

    for i in range(1, SZ + 1):
            for j in range(1, SZ + 1):
                for k in range(1, SZ + 1):
                    maze[t][i][j][k] = gen.maze[i][j][k]

    # calculate their fitness value
    value1.append(f1.count_distance(maze[t]))
    value2.append(f2.count_crossroads(maze[t]))
    value3.append(f3.count_straight_route(maze[t]))
    print(value1[t], value2[t], value3[t])


for generation in range(SZ):
    for i in range(num):
        # select and crossover
        x = sel.select(num, value1, value2, value3)
        y = sel.select(num, value1, value2, value3)
        crs.crossover(maze[x], maze[y])

        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                for l in range(1, SZ + 1):
                    Maze[i][j][k][l] = crs.res[j][k][l]


    # repalce the original datas
    for i in range(num):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                for l in range(1, SZ + 1):
                    maze[i][j][k][l] = Maze[i][j][k][l]

    # mutation
    for i in range(num):
        mut.mutate(maze[i])
        maze[i][mut.kx][mut.ky][mut.kz] = 1
        value1[i] = f1.count_distance(maze[i])
        value2[i] = f2.count_crossroads(maze[i])
        value3[i] = f3.count_straight_route(maze[i])

