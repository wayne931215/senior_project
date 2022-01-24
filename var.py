SZ = 20
N = 10
generation = 10
MAX = SZ * SZ * (SZ - 1) * 3
dirr = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
mrate = 0.5 #mutation rate
arate = 1 #ancestor rate

def print_maze(maze):
    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                print(maze[i][j][k], end=' ')
            print()
        print()

def proper(x, y, z):
    if x < 1 or x > SZ or y < 1 or y > SZ or z < 1 or z > SZ:
        return False
    return True