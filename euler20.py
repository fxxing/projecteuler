import math


def solve(n):
    return sum([int(d) for d in str(math.factorial(n))])


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve(100)")