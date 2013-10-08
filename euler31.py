UNIT = [200, 100, 50, 20, 10, 5, 2, 1]


def count(n, t):
    if t == len(UNIT) - 1:
        return 1
    c = 0
    u = UNIT[t]
    for i in range(n / u + 1):
        c += count(n - i * u, t + 1)
    return c


def solve(n):
    return count(n, 0)


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve(200)")