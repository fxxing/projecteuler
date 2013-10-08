#!/usr/bin/env python
# coding: utf-8

M = 999
F1 = 3
F2 = 5


def sumf(f):
    return int(M / f / 2.0 * (f + M / f * f))


def solve():
    s = sumf(F1)  # sum of 3
    s += sumf(F2)  # sum of 5
    s -= sumf(F1 * F2)  # sum of 3 * 5, it calulate twice, subtract once
    return int(s)


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve()")