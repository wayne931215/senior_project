import random

"""array 即為生成的maze初代，其並沒有外牆(自行想像外面還有一層障礙物包裹住迷宮)，以0,0,0為起點，
以(size-1, size-1, size-1)為終點，其ancestor_rate表示地圖中除了起點和終點外障礙物佔有的比例
其size表示此正方體迷宮的邊長大小，兩者皆是可調整的參數。生成的初代保證起點到終點必有至少一條路
"""

ancestor_rate = 0.6
size = 5

isfind = 0
# [[[0 for k in range(size)] for j in range(size)] for i in range(size)]
# visited = [[0]*size for i in range(size)]
array = [[[0 for k in range(size+1)] for j in range(size+1)] for i in range(size+1)]
visited = [[[0 for k in range(size+1)] for j in range(size+1)] for i in range(size+1)]
isfind = 0

def dfs(array, x, y, z, aimx, aimy, aimz, visited):
    global isfind
    
    if isfind:
        return
    if x < 1 or x > size or y < 1 or y > size or z < 1 or z > size:
        return
    if visited[x][y][z] == 1 :
        return
    if x == aimx and y == aimy and z == aimz:
        isfind = 1
        
        return
    
    visited[x][y][z] = 1
    dfs(array, x+1, y, z, aimx, aimy, aimz, visited)
    dfs(array, x-1, y, z, aimx, aimy, aimz, visited)
    dfs(array, x, y+1, z, aimx, aimy, aimz, visited)
    dfs(array, x, y-1, z, aimx, aimy, aimz, visited)
    dfs(array, x, y, z+1, aimx, aimy, aimz, visited)
    dfs(array, x, y, z-1, aimx, aimy, aimz, visited)
     
while True:
    for i in range(size):
        for j in range(size):
            for k in range(size):
                visited[i+1][j+1][k+1] = 0
                array[i+1][j+1][k+1] = 0
            
    index_list = []
    for i in range(1, size * size*size-1, 1):
        index_list.append(i)

    random.shuffle(index_list)
    
    for i in range(int(size*size*size*ancestor_rate)):
        #print(index_list[i], end=' ')
        z = index_list[i] // (size*size)
        y = (index_list[i] % (size*size)) // size
        x = index_list[i] % size
        #print ("(",z, y, x,")", end=' ')
        visited[z+1][y+1][x+1] = 1
        array[z+1][y+1][x+1] = 1
    print()
    dfs(array, 1, 1, 1, size, size, size, visited)
    
    if isfind:
        break     
"""
print("Has generated a ancestor genetic map.")
print() 
for i in range (size):
    for j in range (size):
        for k in range(size):
            print(array[i+1][j+1][k+1], end=' ')
        print() 
    print()
    print()
"""
