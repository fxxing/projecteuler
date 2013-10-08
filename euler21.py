from util import sum_factor


def solve():
    amicable_numbers = []

    for n in range(10000):
        if n in amicable_numbers:
            continue
        s = sum_factor(n)
        if s != n and n == sum_factor(s):
            if n not in amicable_numbers:
                amicable_numbers.append(n)
            if s not in amicable_numbers:
                amicable_numbers.append(s)
    return sum(amicable_numbers)


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")