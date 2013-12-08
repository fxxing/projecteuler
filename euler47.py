import math
from util import primes2

primes = primes2(1000000)


def factorize(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n //= 2
    limit = math.sqrt(n + 1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n //= i
            limit = math.sqrt(n + i)
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res


def solve():
    count_down = 4
    n = 650
    while 1:
        if len(set(factorize(n))) == 4:
            count_down -= 1
            if count_down == 0:
                return n - 3
        else:
            count_down = 4
        n += 1


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")