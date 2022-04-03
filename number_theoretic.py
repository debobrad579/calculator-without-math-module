ceil = lambda x: int(x) + 1 if x > int(x) else int(x)
floor = lambda x: int(x) - 1 if x < int(x) else int(x)
gcd = lambda x, y: gcd(y, x % y) if y != 0 else x
lcm = lambda x, y: x * y / gcd(x, y)
abs = lambda x: x if x >= 0 else -x
factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
double_factorial = lambda x: 1 if x <= 0 else x * double_factorial(x - 2)
