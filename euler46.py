from util import primes2, is_prime


def solve():
    p = 33
    while 1:
        p += 2
        if not is_prime(p):

            for i in range(1, p / 2 + 1):
                if is_prime(p - 2 * i * i):
                    break
            else:
                return p


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")