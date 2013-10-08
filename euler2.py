#!/usr/bin/env python
# coding: utf-8

M = 4000000


def sumf(f):
    return int(M / f / 2.0 * (f + M / f * f))


def solve():
    x, y = 1, 2
    s = 0
    while y < M:
        if y % 2 == 0:
            s += y
        t = y
        y += x
        x = t
    return s


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve()")