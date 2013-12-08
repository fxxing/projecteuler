from util import primes, is_prime


def is_removeable_prime(n):
    if not is_prime(n):
        return False
    sn = str(n)
    for i in range(1, len(sn)):
        if not is_prime(int(sn[i:])):
            return False
        if not is_prime(int(sn[:i])):
            return False
    return True


def solve():
    print 'start'
    s = 0
    p = primes()
    n = p.next()
    cd = 11
    while cd > 0:
        if n < 11:
            n = p.next()
            continue
        if is_removeable_prime(n):
            print n
            cd -= 1
            s += n
        n = p.next()
    return s


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")