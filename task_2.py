"""
 Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...
@type_logger
def calc_cube(x):
   return x ** 3
a = calc_cube(5)
5: <class 'int'>

"""


def type_logger(func):
    def wrapper(*args):
        result = f'{func.__name__}('
        for a in args:
            result +=f'{str(a)}: {str(type(a))}'

        result += f")"
        print(result)
        return func(*args)
    return wrapper

@type_logger
def calc_cube(x):
    return x**3

print(calc_cube(5))