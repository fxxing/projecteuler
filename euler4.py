#!/usr/bin/env python
# coding: utf-8

MIN = 99
MAX = 999


def solve():
    m = 0
    for x in xrange(MAX, MIN, -1):
        for y in xrange(MAX, MIN, -1):
            n = x * y
            s = str(n)
            if s == s[::-1] and n > m:
                m = n
    return m


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve()")