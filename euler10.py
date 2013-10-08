#!/usr/bin/env python
# coding: utf-8
import math

M = 2000000


def solve():
    n = 11
    s = 17
    while n < M:
        for i in xrange(3, int(math.sqrt(n)) + 1):
            if n % i == 0:
                break
        else:
            s += n
        n += 2
    return s


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve()")