import math


def is_triangluar(n):
    x = (math.sqrt(1 + 8 * n) - 1.0) / 2.0
    return int(x) == x


def is_pentagonal(n):
    x = (math.sqrt(1 + 24 * n) + 1.0) / 6.0
    return int(x) == x


def is_hexagonal(n):
    x = (math.sqrt(1 + 8 * n) + 1.0) / 4.0
    return int(x) == x


def solve():
    i = 144
    while 1:
        h = i * (2 * i - 1)
        if is_pentagonal(h) and is_triangluar(h):
            return h
        i += 1


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")