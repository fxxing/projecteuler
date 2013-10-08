import cProfile


# very fast
def solve():
    sa = set()
    sb = set()
    for n in xrange(2, 99):
        l = str(n)
        if len(l) == len(set(l)):
            sa.add(n)
    for n in xrange(123, 9877):
        l = str(n)
        if len(l) == len(set(l)):
            sb.add(n)
    rs = set()
    for a in sa:
        for b in sb:
            if b > 9999.0 / a:
                break
            x = a * b
            s = str(a) + str(b) + str(x)
            if "0" not in s and len(s) == 9 and len(set(s)) == 9:
                print a, b, x
                rs.add(x)
    return sum(rs)


def solve2():
    ran = xrange(0, 10)
    possa = [10 * a + b for a in ran for b in ran if a != b]
    possb = []
    for a in xrange(100, 9999):
        x = str(a)
        y = set(x)
        if len(x) == len(y):
            possb.append(a)
    sol = []
    for a in possa:
        for b in possb:
            if b < max(a, 1000.0 / a):
                continue
            if b > 9999.0 / a:
                break
            c = a * b
            if "".join(sorted(str(a) + str(b) + str(c))) == "123456789":
                sol.append(c)
    sol = set(sol)
    print sum(sol)


if __name__ == "__main__":
    cProfile.run("print solve()")
