SZ = 20
N = 10
generation = 10
MAX = SZ * SZ * (SZ - 1) * 3
dirr = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
mrate = 1 #mutation rate
arate = 0.5 #ancestor rate

def print_maze(maze):
    f = open('output.txt', 'w')
    f2 = open('output2.txt', 'w')

    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                print("grid[", (i-1) * SZ * SZ + (j-1) * SZ + (k-1), "].val =",int(maze[i][j][k]), end=";", file=f)
                print(int(maze[i][j][k]), end=' ', file=f2)
            print(file=f2)
        print(file=f)
        print(file=f2)

    f.close()

def proper(x, y, z):
    if x < 1 or x > SZ or y < 1 or y > SZ or z < 1 or z > SZ:
        return False
    return True
