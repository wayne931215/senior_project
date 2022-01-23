import random
import var
import time
import FitnessValue1 as f1
import numpy as np

ancestor_rate = 0.5
SZ = var.SZ
random.seed(time.time())

maze = np.zeros((SZ + 1, SZ + 1, SZ + 1))

def generate():
    while True:
        for i in range(SZ):
            for j in range(SZ):
                for k in range(SZ):
                    maze[i+1][j+1][k+1] = 0

        index_list = []
        for i in range(1, SZ*SZ*SZ - 1):
            index_list.append(i)

        random.shuffle(index_list)

        for i in range(int(SZ*SZ*SZ*ancestor_rate)):
            z = index_list[i] // (SZ*SZ)
            y = (index_list[i] % (SZ*SZ)) // SZ
            x = index_list[i] % SZ
            maze[z+1][y+1][x+1] = 1

        if f1.count_distance(maze) != 0:
            return maze

generate()