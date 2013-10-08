from datetime import date
from dateutil.relativedelta import relativedelta


def solve():
    dt = date(1901, 1, 1)
    dl = date(2000, 12, 31)
    dd = relativedelta(months=1)

    count = 0
    while dt < dl:
        if dt.weekday() == 6:
            count += 1
        dt += dd

    return count


if __name__ == "__main__":
    import cProfile

    cProfile.run("print solve()")