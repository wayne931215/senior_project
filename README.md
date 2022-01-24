# Senior_project
**Leo is gay.**

## module
the size of maze (SZ) <br>
the number of mazes (N) <br>
print the maze <br>
ancestor rate of passages (arate) <br>
rate of mutation (mrate) <br>

## gen.py
use dfs to generate ancestor mazes 

## Fitness value
1. the distance from S to E <br>
2. the number of crossroads <br>
3. the number of straight routes (considering its length) <br>

## sel.py
randomly pick two mazes to crossover(wheel selection)

## crs.py
first denote S as (1, 1, 1), E as (SZ + 1, SZ + 1, SZ + 1) in the maze <br>
i. pick 2 mazes (A and B) <br>
ii. randomly pick a 2D plain in the maze and rebuild the plain <br>
iii. maze A builds up the upper part of the new maze; maze B builds up the lower part <br>
iv. repeat step i. and ii. until S and E are connected <br>

## mut.py
i. find the coordinates of spaces that are only reachable through one direction <br>
ii. randomly pick one and turn it into wall <br>