def solve():
    p = 1
    for n in range(10, 100):
        for d in range(n + 1, 100):
            sn = str(n)
            sd = str(d)
            if (float(sd[1]) != 0 and float(n) / d == float(sn[0]) / float(sd[1]) and sn[1] == sd[0]) or \
                    (float(sd[0]) != 0 and float(n) / d == float(sn[1]) / float(sd[0]) and sn[0] == sd[1]):
                p *= float(d) / n
    return int(p)


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve()")