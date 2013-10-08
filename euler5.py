#!/usr/bin/env python
# coding: utf-8

from fractions import gcd


def lcm(a, b):
    return (a * b) // gcd(a, b)


def solve():
    n = 1
    for i in range(2, 21):
        n = lcm(n, i)
    return n


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve()")