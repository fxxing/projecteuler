from util import get_content


def score_name(name):
    return sum([ord(c) - 64 for c in name])


def solve(names):
    s = 0
    for i, name in enumerate(names):
        s += sum([ord(c) - 64 for c in name]) * (i + 1)
    return s


if __name__ == "__main__":
    import cProfile

    text = get_content("http://projecteuler.net/project/names.txt")
    names = [name.replace('"', '').strip() for name in text.split(',')]
    names.sort()
    cProfile.run('print solve(names)')