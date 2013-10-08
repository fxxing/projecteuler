def solve(n):
    s = 1
    for i in range(3, n + 1, 2):
        s += 4 * i * i - 6 * i + 6
    return s


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve(1001)")