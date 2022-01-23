import numpy as np
import random
import gen


def select(n, val):
    pos = []
    s = 0
    for i in range(n):
        s += val[i]
        pos.append(s)

    a = random.uniform(0, s)
    l = 0
    r = n
    m = (l + r) // 2

    while l < r:
        m = (l + r) // 2
        if pos[m] >= a:
            r = m
        else:
            l = m + 1

    return l
