from itertools import permutations


def solve():
    for i, x in enumerate(permutations("0123456789")):
        if i == 999999:
            return "".join([str(d) for d in x])


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")