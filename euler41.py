from itertools import permutations
from util import is_prime


def solve():
    m = 1
    for i in range(1, 10):
        for n in permutations("".join([str(d) for d in range(1, i + 1)])):
            x = int("".join(n))
            if is_prime(x):
                m = x

    return m


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")