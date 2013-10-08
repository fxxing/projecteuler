def solve(limit):
    cache = {2: 2}

    mc = 0
    mn = 0
    for n in xrange(2, limit):
        x = n
        c = 1
        while x != 1:
            if x in cache:
                c += cache[x] - 1
                break
            if x % 2 == 0:
                x /= 2
                c += 1
            else:
                x = (x * 3 + 1) / 2
                c += 2

        if n not in cache:
            cache[n] = c
        if c > mc:
            mc = c
            mn = n
    return mn, mc


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve(1000000)")