from itertools import permutations
from util import is_prime, get_content, primes2


def is_unique(n):
    return


def solve2():
    px = primes2(19)
    dc = {}
    for p in px:
        s = set()
        for h in range(12/p or 1, 1000/p + 2):
            x = h * p
            xs = "%03d" % x
            if 11 < x < 988 and len(xs) == len(set(xs)):
                s.add(xs)
        dc[p] = tuple(s)

    sn = 0
    for a in dc[2]:
        for b in dc[7]:
            for c in dc[17]:
                s = a + b + c
                if len(s) != len(set(s)):
                    continue
                for i, p in enumerate(px):
                    if i in (0, 3, 6):
                        continue
                    if int(s[i:i+3]) % p != 0:
                        break
                else:
                    for h in [str(d) for d in range(1, 10)]:
                        if h in s:
                            continue
                        else:
                            print h + s
                            sn += int(h + s)
    return sn

if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve2()")