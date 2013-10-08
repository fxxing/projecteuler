import urllib2
import math


def get_content(url):
    request = urllib2.Request(url)
    content = urllib2.urlopen(request).read()
    return content


def sum_factor(n):
    s = 1
    x = int(math.sqrt(n)) or 1
    for f in xrange(2, x + 1):
        if n % f == 0:
            s += f
            s += n / f
    if x * x == n:
        s -= x
    return s


def prime():
    yield 1
    yield 2
    yield 3

    n = 5
    while 1:
        if is_prime(n):
            yield n
        n += 2


def is_prime(n):
    x = int(math.sqrt(n)) or 1
    for f in xrange(2, x + 1):
        if n % f == 0:
            return False
    else:
        return True
