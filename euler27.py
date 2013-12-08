from util import primes, is_prime, primes2


def count_prime(a, b):
    n = 0
    while 1:
        if is_prime(abs(n * n + a * n + b)):
            n += 1
        else:
            return n


def solve():
    m = [0, 0, 0]

    def max_prime(a, b):
        c = count_prime(a, b)
        if c > m[0]:
            m[0] = c
            m[1] = a
            m[2] = b

    pa = primes()
    a = pa.next()
    while a < 1000:
        pb = primes()
        b = pb.next()
        while b < 1000:
            max_prime(a, b)
            max_prime(a, -b)
            max_prime(-a, -b)
            max_prime(-a, b)
            b = pb.next()
        a = pa.next()
    return m


def solve2():
    m = [0, 0, 0]

    def max_prime(a, b):
        c = count_prime(a, b)
        if c > m[0]:
            m[0] = c
            m[1] = a
            m[2] = b

    ps = primes2(1000)
    for a in ps:
        for b in ps:
            max_prime(a, b)
            max_prime(a, -b)
            max_prime(-a, -b)
            max_prime(-a, b)
    return m


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")
