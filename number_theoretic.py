def ceil(x: float) -> int:
    return int(x) + 1 if x > int(x) else int(x)


def floor(x: float) -> int:
    return int(x) - 1 if x < int(x) else int(x)


def gcd(x: int, y: int) -> int:
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def lcm(x: int, y: int) -> int:
    return x * y / gcd(x, y)


def abs(x):
    return x if x >= 0 else -x


def factorial(x: int) -> int:
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


def double_factorial(x: int) -> int:
    if x <= 0:
        return 1
    else:
        return x * double_factorial(x - 2)
