from util import primes2, is_prime


def solve():
    for p in primes2(3340):
        if p < 1000:
            continue
        p1 = p + 3330
        p2 = p + 6660
        if not is_prime(p1) or not is_prime(p2):
            continue
        if sorted(str(p)) == sorted(str(p1)) == sorted(str(p2)):
            return str(p) + str(p1) + str(p2)


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")