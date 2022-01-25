# Senior_project

## module
the size of maze (SZ)\
the number of mazes (N)\
print the maze\
ancestor rate of passages (arate)\
rate of mutation (mrate)\

## gen.py
use dfs to generate ancestor mazes 

## Fitness value
1. the distance from S to E
2. the number of crossroads
3. the number of straight routes (considering its length)

## sel.py
randomly pick two mazes to crossover(wheel selection)

## crs.py
first denote S as (1, 1, 1), E as (SZ + 1, SZ + 1, SZ + 1) in the maze\
i. pick 2 mazes (A and B)\
ii. randomly pick a 2D plain in the maze and rebuild the plain\
iii. maze A builds up the upper part of the new maze; maze B builds up the lower part\
iv. repeat step i. and ii. until S and E are connected\

## mut.py
i. find the coordinates of spaces that are only reachable through one direction\
ii. randomly pick one and turn it into wall\