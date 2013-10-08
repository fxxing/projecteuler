import math


def solve(n):
    f1 = math.factorial(n)
    f2 = math.factorial(2 * n)
    return f2 / f1 / f1


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve(20)")