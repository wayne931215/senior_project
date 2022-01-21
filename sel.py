import numpy as np
import random as rd
import gen


def select(n, val1, val2, val3):
    pos = []
    s = 0
    for i in range(n):
        s += val[i]
        pos.append(s)

    a = rd.random(0, s)
    l = 0
    r = n
    m = (l + r) // 2

    while l < r:
        if pos[m] >= a:
            r = m
        else:
            l = m + 1

    return l
