from itertools import combinations
from operator import add, sub
import math


def pentagonal(n):
    return n * (3 * n - 1) / 2


def is_pentagonal(n):
    x = (math.sqrt(1 + 24 * n) + 1.0) / 6.0
    return int(x) == x


def solve():
    k = 1
    while 1:
        pk = k * (3 * k - 1) / 2
        for j in range(k - 1, 0, -1):
            pj = j * (3 * j - 1) / 2
            if is_pentagonal(pk + pj) and is_pentagonal(pk - pj):
                return k, j, abs(pk - pj)
        k += 1


def solve2():
    pentagonals = set(pentagonal(n) for n in range(1, 3000))
    c = combinations(pentagonals, 2)
    for p in c:
        if p[0] + p[1] in pentagonals and abs(p[0] - p[1]) in pentagonals:
            print abs(sub(*p))


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve2()")