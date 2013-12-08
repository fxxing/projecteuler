from itertools import permutations
from util import is_prime, get_content


def solve(words):
    max_length = max([len(word) for word in words])
    max_value = 26 * max_length
    trians = []
    for i in xrange(1, max_value):
        n = i * (i + 1) / 2
        if n > max_value:
            break
        trians.append(n)
    print trians
    c = 0
    for word in words:
        if sum([ord(w)-64 for w in word]) in trians:
            c += 1

    return c


if __name__ == "__main__":
    import cProfile

    text = get_content("http://projecteuler.net/project/words.txt")
    words = [word.replace('"', '').strip() for word in text.split(',')]

    cProfile.run("print solve(words)")