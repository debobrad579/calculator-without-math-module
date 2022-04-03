from util import format_complex
from constants import pi, e, i
from exponential import sqrt, ln


def degrees(x):
    return round(x * (180 / pi), 2)


def radians(x):
    return x * (pi / 180)


@format_complex
def sin(x):
    return 0.5 * i * e ** (-i * x) - 0.5 * i * e ** (i * x)


@format_complex
def cos(x):
    return 0.5 * e ** (-i * x) + 0.5 * e ** (i * x)


@format_complex
def tan(x):
    return sin(x) / cos(x)


@format_complex
def asin(x):
    return -i * ln(sqrt(1 - x ** 2) + i * x)


@format_complex
def acos(x):
    return pi / 2 + i * ln(sqrt(1 - x ** 2) - x * i)


@format_complex
def atan(x):
    return 0.5 * i * ln(1 - i * x) - 0.5 * i * ln(1 + i * x)


@format_complex
def atan2(y, x):
    return atan(y / x)


@format_complex
def sec(x):
    return 1 / cos(x)


@format_complex
def csc(x):
    return 1 / sin(x)


@format_complex
def cot(x):
    return 1 / tan(x)


@format_complex
def asec(x):
    return acos(1 / x)


@format_complex
def acsc(x):
    return asin(1 / x)


@format_complex
def acot(x):
    return atan(1 / x)


@format_complex
def sinh(x):
    return (e ** x - e ** (-x)) / 2


@format_complex
def cosh(x):
    return (e ** x + e ** (-x)) / 2


@format_complex
def tanh(x):
    return sinh(x) / cosh(x)


@format_complex
def asinh(x):
    return ln(x + sqrt(x ** 2 + 1))


@format_complex
def acosh(x):
    return ln(x + sqrt(x ** 2 - 1))


@format_complex
def atanh(x):
    return 0.5 * ln((1 + x) / (1 - x))


@format_complex
def sech(x):
    return 1 / cosh(x)


@format_complex
def csch(x):
    return 1 / sinh(x)


@format_complex
def coth(x):
    return 1 / tanh(x)


@format_complex
def asech(x):
    return acosh(1 / x)


@format_complex
def acsch(x):
    return asinh(1 / x)


@format_complex
def acoth(x):
    return atanh(1 / x)
