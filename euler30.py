def solve():
    ds = []
    for i in xrange(2, 9 ** 5 * 4):
        x = i
        s = 0
        while x > 0:
            x, l = divmod(x, 10)
            if l > 0:
                s += l ** 5
        if s == i:
            ds.append(s)
    print ds
    return sum(ds)


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")