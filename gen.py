import random
import var

"""maze 即為生成的maze初代，其並沒有外牆(自行想像外面還有一層障礙物包裹住迷宮)，以1,1,1為起點，
以(SZ, SZ, SZ)為終點，其ancestor_rate表示地圖中除了起點和終點外障礙物佔有的比例
其SZ表示此正方體迷宮的邊長大小，兩者皆是可調整的參數。生成的初代保證起點到終點必有至少一條路
"""

ancestor_rate = 0.5
SZ = var.SZ

# [[[0 for k in range(SZ)] for j in range(SZ)] for i in range(SZ)]
# visited = [[0]*SZ for i in range(SZ)]
maze = [[[0 for k in range(SZ+1)] for j in range(SZ+1)]
         for i in range(SZ+1)]
visited = [[[0 for k in range(SZ+1)]
            for j in range(SZ+1)] for i in range(SZ+1)]
isfind = 0.6


def dfs(x, y, z):
    global isfind
    if isfind:
        return
    if visited[x][y][z] == 1:
        return
    if x == SZ and y == SZ and z == SZ:
        isfind = 1
        return

    visited[x][y][z] = 1
    if x < SZ:
        dfs(x+1, y, z)
    if x > 1:
        dfs(x-1, y, z)
    if y < SZ:
        dfs(x, y+1, z)
    if y > 1:
        dfs(x, y-1, z)
    if z < SZ:
        dfs(x, y, z+1)
    if z > 1:
        dfs(x, y, z-1)


def generate():
    while True:
        for i in range(SZ):
            for j in range(SZ):
                for k in range(SZ):
                    visited[i+1][j+1][k+1] = 0
                    maze[i+1][j+1][k+1] = 0

        index_list = []
        for i in range(1, SZ*SZ*SZ - 1, 1):
            index_list.append(i)

        random.shuffle(index_list)

        for i in range(int(SZ*SZ*SZ*ancestor_rate)):
            # print(index_list[i], end=' ')
            z = index_list[i] // (SZ*SZ)
            y = (index_list[i] % (SZ*SZ)) // SZ
            x = index_list[i] % SZ
            # print ("(",z, y, x,")", end=' ')
            visited[z+1][y+1][x+1] = 1
            maze[z+1][y+1][x+1] = 1
        dfs(1, 1, 1)
        if isfind:
            return maze
