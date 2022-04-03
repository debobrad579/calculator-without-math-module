from constants import i


def basically_int(x):
    return int(x) if int(x) - 0.000001 < x < int(x) + 0.000001 else x

def basically_zero(x):
    return -0.000001 < x < 0.000001


def format_complex(func):
    def wrapper(x):
        result = func(x)
        real = basically_int(result.real)
        imag = basically_int(result.imag)

        if basically_zero(imag):
            return real
        
        if basically_zero(real):
            return imag * i

        return real + imag * i
    
    return wrapper
