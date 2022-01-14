SZ = 20


def print_maze(maze):
    for i in range(1, SZ + 1):
        for j in range(1, SZ + 1):
            for k in range(1, SZ + 1):
                print(maze[i][j][k], end=' ')
            print()

        print()
