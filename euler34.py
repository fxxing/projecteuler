import math


def solve():
    s = 0
    for n in range(3, math.factorial(9)):
        f = sum([math.factorial(int(d)) for d in str(n)])
        if f == n:
            s += n
    return s


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")