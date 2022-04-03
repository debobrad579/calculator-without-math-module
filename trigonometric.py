from util import format_complex
from constants import pi, e, i
from exponential import sqrt, ln

degrees = lambda x: x * (180 / pi)
radians = lambda x: x * (pi / 180)

sin = format_complex(lambda x: 0.5 * i * e ** (-i * x) - 0.5 * i * e ** (i * x))
cos = format_complex(lambda x: 0.5 * e ** (-i * x) + 0.5 * e ** (i * x))
tan = format_complex(lambda x: sin(x) / cos(x))
sec = format_complex(lambda x: 1 / cos(x))
csc = format_complex(lambda x: 1 / sin(x))
cot = format_complex(lambda x: cos(x) / sin(x))
sinh = format_complex(lambda x: (e ** x - e ** (-x)) / 2)
cosh = format_complex(lambda x: (e ** x + e ** (-x)) / 2)
tanh = format_complex(lambda x: sinh(x) / cosh(x))
sech = format_complex(lambda x: 1 / cosh(x))
csch = format_complex(lambda x: 1 / sinh(x))
coth = format_complex(lambda x: cosh(x) / sinh(x))
asin = format_complex(lambda x: -i * ln(i * x + sqrt(1 - x ** 2)))
acos = format_complex(lambda x: pi / 2 - asin(x))
atan = format_complex(lambda x: i * ln(i * x + sqrt(1 - x ** 2)))
atan2 = format_complex(lambda y, x: atan(y / x))
asec = format_complex(lambda x: acos(1 / x))
acsc = format_complex(lambda x: asin(1 / x))
acot = format_complex(lambda x: pi / 2 - atan(x))
asinh = format_complex(lambda x: i * ln(x + sqrt(x ** 2 + 1)))
acosh = format_complex(lambda x: i * ln(x + sqrt(x ** 2 - 1)))
atanh = format_complex(lambda x: i * ln((1 + x) / (1 - x)))
asech = format_complex(lambda x: i * ln(1 / x + sqrt(1 - 1 / x ** 2)))
acsch = format_complex(lambda x: i * ln(1 / x - sqrt(1 - 1 / x ** 2)))
acoth = format_complex(lambda x: (1 + x) / (1 - x))
