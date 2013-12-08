import math


def solve():
    count = {}
    for a in range(1, 333):
        for b in range(a, 666):
            c = math.sqrt(a * a + b * b)
            if int(c) == c:
                p = int(a + b + c)
                if p in count:
                    count[p] += 1
                else:
                    count[p] = 1
    mk = 0
    mc = 0
    for k in count:
        if count[k] > mc:
            mk = k
            mc = count[k]
    print mk, mc
    return mk


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")