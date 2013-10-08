#!/usr/bin/env python
# coding: utf-8
import math


# This can be done within 300ms, this solution:
# real	0m5.389s
# user	0m5.371s
# sys   0m0.015s
#
# need impovement


def solve(limit):
    s = 7
    n = 28
    while 1:
        c = 2
        x = int(math.sqrt(n))
        for f in xrange(2, x + 1):
            if n % f == 0:
                c += 2
        if n % x == 0:
            c -= 1
        if c > limit:
            return n
        s += 1
        n += s


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve(500)")