def solve():

    md = 0
    for n in xrange(1, 9999):
        s = ""
        for i in range(1, 10):
            s += str(n * i)
            if "0" in s:
                break
            if len(s) == 9:
                if len(set(s)) == 9:
                    x = int(s)
                    if x > md:
                        md = x
                else:
                    break
            elif len(s) > 9:
                break
    return md


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")