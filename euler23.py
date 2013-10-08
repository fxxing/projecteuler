from util import sum_factor


def solve():
    abundants = []
    limit = 28124
    for n in xrange(1, limit):
        if n < sum_factor(n):
            abundants.append(n)

    s = set()
    for i in range(len(abundants)):
        for j in range(i, len(abundants)):
            h = abundants[i] + abundants[j]
            if h > limit:
                break
            s.add(h)
    u = set(range(1, limit)).difference(s)
    return sum(u)


if __name__ == "__main__":
    import cProfile
    #print sum_factor(18)
    cProfile.run("print solve()")