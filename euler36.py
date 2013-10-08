def is_palindromic(n):
    sn = str(n)
    if not sn == sn[::-1]:
        return False
    sb = bin(n)[2:]
    if not sb == sb[::-1]:
        return False
    return True


def solve():
    s = 0
    for i in xrange(1, 1000000):
        if is_palindromic(i):
            print i
            s += i
    return s


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")