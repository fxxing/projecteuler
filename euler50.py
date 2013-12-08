from util import primes2, is_prime

primes = primes2(1000000)


def max_count(n):
    factors = []
    m = 0
    s = 0
    for p in primes:
        if p > n:
            break
        factors.append(p)
        s += p
        while s > n:
            s -= factors.pop(0)
        if s == n:
            l = len(factors)
            if l > m:
                m = l
            s -= factors.pop(0)
        assert s == sum(factors)
    return m


# too too too slow
def solve():
    mc = 0
    mn = 0
    for n in primes:
        if n < 997000:
            continue
        c = max_count(n)
        if c > mc:
            print n, c
            mc = c
            mn = n
    return mc, mn


# this one is trick, not consider all results, but it works
def solve2():
    chain = []
    for start in range(10):
        seq = primes[start:]
        i = 0
        total = 0
        for prime in seq:
            total += prime
            if total > 1000000:
                break
            i += 1
            if total in primes:
                c = seq[:i]
                if len(c) > len(chain):
                    chain = c
    return sum(chain)


if __name__ == "__main__":
    import cProfile
    #print max_count(41)
    cProfile.run("print solve2()")