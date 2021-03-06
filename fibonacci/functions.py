import math


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def color(n):
    return [(102, 204, 255), (102, 204, 255), (255, 0, 102), (153, 255, 51),
            (0, 51, 204), (255, 0, 255), (0, 102, 0),
            (51, 204, 204), (255, 102, 0), (153, 102, 51),
            (102, 102, 153), (204, 51, 0), (204, 255, 204),
            (102, 102, 255), (153, 0, 51), (255, 255, 0),
            (153, 0, 255), (153, 51, 51), (204, 255, 153)][n]


def distance_to_fib(point, f):
    return ((point[0] - f.pos[0]) ** 2 + (point[1] - f.pos[1]) ** 2) ** 0.5


def reverse_fib(n):
    return round(2.078087 * math.log(n) + 1.672276)
