from constants import i

basically_int = lambda x: int(x) if int(x) - 0.000001 < x < int(x) + 0.000001 else x


def format_complex(func):
    def wrapper(x):
        result = func(x)

        if not isinstance(result, complex):
            return result

        real = basically_int(result.real)
        imag = basically_int(result.imag)

        if imag == 0:
            return real
        
        if real == 0:
            return imag * i

        return real + imag * i
    
    return wrapper


def append_multiplication(string):
    string = string.replace("ial", "zzl").replace("eil", "xxl")

    for i in ["0", "1", "2", "3", "4", "5","6", "7", "8", "9", ")", "e", "i"]:
        for j in ["(", "e", "i","p", "s", "c", "t", "a"]:
                string = string.replace(f"{i}{j}", f"{i}*{j}")
    
    return string.replace("zzl", "ial").replace("xxl", "eil")
