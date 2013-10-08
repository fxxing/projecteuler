#!/usr/bin/env python
# coding: utf-8


def solve(o):
    c = 1
    n = 1
    while 1:
        n += 2
        for i in xrange(3, n / 2):
            if n % i == 0:
                break
        else:
            c += 1
            if c == o:
                return n


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve(10001)")