from util import format_complex
from constants import i


def sqrt(x):
    return x ** 0.5 if x >= 0 else abs(x) ** 0.5 * i


def log(x: float, base: float) -> float:
    result = 0
    y = x
    n = 1

    while base ** n != 1:
        while y >= base ** n:
            y /= base ** n
            result += n

        n /= base
        
    return result


@format_complex
def ln(x):
    n = 100000000.0
    return n * ((x ** (1/n)) - 1)
