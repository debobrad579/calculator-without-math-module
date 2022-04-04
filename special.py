from number_theoretic import factorial
from exponential import ln

gamma = lambda x: factorial(x - 1)
lgamma = lambda x: ln(abs(gamma(x)))
