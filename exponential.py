from util import format_complex
from constants import e, i

sqrt = lambda x: x ** 0.5
nth_root = lambda x, n: x ** (1 / n)
pow = lambda x, y: x ** y
exp = lambda x: e ** x
ln = format_complex(lambda x: 100000000.0 * ((x ** (1/100000000.0)) - 1))


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
