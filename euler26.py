#!/usr/bin/env python
# coding: utf-8


def cycle_count(n):
    f = 1
    lefts = []
    while 1:
        while f < n:
            f *= 10
        f = f % n
        if f == 0:
            return 0
        else:
            if f in lefts:
                return len(lefts) - lefts.index(f)
            else:
                lefts.append(f)


def solve():
    mc = mn = 0
    for n in xrange(2, 1000):
        c = cycle_count(n)
        if c > mc:
            mc = c
            mn = n
    return mn


if __name__ == "__main__":
    import cProfile

    #print cycle_count(70)
    cProfile.run("print solve()")