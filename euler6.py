#!/usr/bin/env python
# coding: utf-8


def solve(n):
    s1 = s2 = 0
    for i in range(1, n + 1):
        s1 += i * i
        s2 += i
    return s2 * s2 - s1


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve(100)")