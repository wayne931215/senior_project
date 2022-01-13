import numpy as np
import random as rd
import ancestor_map_gen as gen

def select():
    pos = []
    s = 0
    for i in range(gen.num):
        s += gen.val[i]
        pos.append(s)
        
    a = rd.random(0, s)
    l = 0
    r = gen.num
    m = (l + r) // 2

    while l < r:
        if pos[m] >= a:
            r = m
        else:
            l = m + 1

    return l

