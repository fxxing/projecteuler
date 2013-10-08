from util import get_content
from euler18 import solve as solve_triangle


def solve(triangle):
    solve_triangle(triangle)


if __name__ == "__main__":
    import cProfile

    triangle = get_content("http://projecteuler.net/project/triangle.txt")
    cProfile.run('print solve(triangle)')