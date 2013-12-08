import urllib2
import math
import numpy

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
            print f, n/f
            s += f
            s += n / f
    if x * x == n:
        s -= x
    return s


def primes2(n):
    sieve = numpy.ones(n / 3 + (n % 6 == 2), dtype=numpy.bool)
    for i in xrange(1, int(n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k / 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]


def primes():
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


def is_prime2(n):
    return n in primes2(n+1)


def is_prime(n):
    #if n <= PRIMES[-1]:
    #    return n in PRIMES
    #
    if n < 2:
        return False

    x = int(math.sqrt(n)) or 1
    for f in xrange(2, x + 1):
        if n % f == 0:
            return False
    return True


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


if __name__ == "__main__":
    pass
    #print primes2(1000000)
    #p = generate_prime()
    #s = p.next()
    #while s < 10000000:
    #    print s
    #    s = p.next()

        #print is_prime(13)