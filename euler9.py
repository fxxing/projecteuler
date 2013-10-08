#!/usr/bin/env python
# coding: utf-8


def solve(n):
    for b in range(1, n/2):
        for a in range(1, min(n*2/3 - b, b)):
            c = n - a - b
            if a > b or b > c:
                continue
            if a * a + b * b == c * c:
                return a, b, c, a * b * c


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve(1000)")