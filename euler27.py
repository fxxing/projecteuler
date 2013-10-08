from util import prime, is_prime


def count_prime(a, b):
    n = 0
    while 1:
        if is_prime(abs(n * n + a * n + b)):
            n += 1
        else:
            return n


def solve():
    pa = prime()
    m = [0, 0, 0]

    def max_prime(a, b):
        c = count_prime(a, b)
        if c > m[0]:
            m[0] = c
            m[1] = a
            m[2] = b

    a = pa.next()
    while a < 1000:
        pb = prime()
        b = pb.next()
        while b < 1000:
            max_prime(a, b)
            max_prime(a, -b)
            max_prime(-a, -b)
            max_prime(-a, b)
            b = pb.next()
        a = pa.next()
    return m


if __name__ == "__main__":
    import cProfile

    #print cycle_count(70)
    cProfile.run("print solve()")