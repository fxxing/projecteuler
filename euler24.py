# too slow


#noinspection PyDefaultArgument
def permutation(n, r=[]):
    if n == len(r):
        yield []
    l = range(n)
    for k in r:
        l.remove(k)
    for d in l:
        for right in permutation(n, r + [d]):
            yield [d] + right


def solve():
    for i, x in enumerate(permutation(10)):
        if i == 999999:
            return "".join([str(d) for d in x])


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")