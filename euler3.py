#!/usr/bin/env python
# coding: utf-8

N = 600851475143


def solve(n):
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            n /= divisor
            divisor -= 1
        divisor += 1
    return divisor


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve(N)")