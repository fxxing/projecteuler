def ndigital(n):
    x = n
    for i in xrange(1, 10):
        ic = (10 ** i - 10 ** (i - 1)) * i
        if ic >= x:
            l, r = divmod(x, i)
            num = 10 ** (i - 1) + l
            return int(str(num-1)[-1] if r == 0 else str(num)[r - 1])
        else:
            x -= ic


def solve():
    s = 1
    for i in range(7):
        s *= ndigital(10**i)
    return s

if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")