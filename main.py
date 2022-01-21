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
value1 = []
value2 = []
value3 = []

for t in range(num):
    while 1:
        gen.generate()
        for i in range(1, SZ + 1):
            for j in range(1, SZ + 1):
                for k in range(1, SZ + 1):
                    maze[t][i][j][k] = gen.maze[i][j][k]
        if f1.count_distance(maze[t]) != 0:
            break
        
    value1.append(f1.count_distance(maze[t]))
    value2.append(f2.count_crossroads(maze[t]))
    value3.append(f3.count_straight_route(maze[t]))
    print(value1[t], value2[t], value3[t])
