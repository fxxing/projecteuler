from util import is_prime

ps = []


def is_circular(n):
    if n in ps:
        return True
    s = str(n)
    ls = []
    for i in range(len(s)):
        if not is_prime(int(s)):
            return False
        ls.append(int(s))
        s = s[1:] + s[0]
    ps.extend(ls)
    return True


def solve():
    ss = set()
    for n in xrange(2, 1000000):
        if is_circular(n):
            print n
            ss.add(n)
    print ss
    return len(ss)


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")