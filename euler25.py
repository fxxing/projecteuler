#!/usr/bin/env python
# coding: utf-8


def solve():
    x, y = 1, 1
    c = 2
    m = 10 ** 999
    while y < m:
        t = y
        y += x
        x = t
        c += 1
    print x
    print y
    return c


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")