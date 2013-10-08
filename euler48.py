def solve():
    s = 0
    for i in xrange(1, 1001):
        s += i ** i
    return str(s)[-10:]


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")