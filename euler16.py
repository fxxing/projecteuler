def solve(n, p):
    return sum([int(d) for d in str(n ** p)])


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve(2, 1000)")