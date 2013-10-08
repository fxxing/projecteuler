UNIT = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
DECAD = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def num2word(n):
    """
    number to word, only for 0 - 1000
    """""

    if n == 1000:
        return "one thousand"

    x = n
    word = ""

    if x >= 100:
        h, x = divmod(x, 100)
        word += UNIT[h] + " hundred"
    if x > 0 and word:
        word += " and "

    if x >= 20:
        d, x = divmod(x, 10)
        word += DECAD[d - 2]
        if x > 0:
            word += "-" + UNIT[x]

    elif x > 0:
        word += UNIT[x]

    return word


def solve():
    s = 0
    for n in range(1, 1001):
        s += len(num2word(n).replace(" ", "").replace("-", ""))
    return s


if __name__ == "__main__":
    import cProfile
    cProfile.run("print solve()")