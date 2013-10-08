import urllib2
import math

# Why use this make it very slow? it should be faster
#from prime import PRIMES


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


def generate_prime():
    #_index = 0
    yield 2
    #while _index < len(PRIMES):
    #    yield PRIMES[_index]
    #    _index += 1
    #
    n = 3
    while 1:
        if is_prime(n):
            yield n
            #_index += 1
        n += 2


def is_prime(n):
    #if n <= PRIMES[-1]:
    #    return n in PRIMES

    if n < 2:
        return False

    x = int(math.sqrt(n)) or 1
    for f in xrange(2, x + 1):
        if n % f == 0:
            return False
    return True


if __name__ == "__main__":
    #p = generate_prime()
    #s = p.next()
    #while s < 1000000:
    #    print s
    #    s = p.next()

    print is_prime(13)