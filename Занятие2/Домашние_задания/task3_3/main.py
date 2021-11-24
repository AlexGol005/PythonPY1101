import inspect

def arg_type_int(fn):
    def wrapper(*args, **kwargs):
        for arg in args:
            try:
                (_ for _ in arg)
            except ...:  # fixme
                raise TypeError("Объект <название или номер позиционного аргумента> <значение аргумента> не является итерируемым")

            result = fn(*args, **kwargs)
            return result
    return wrapper

if __name__ == "__main__":
    @arg_type_int
    def a(n):
        print(n)


    def foo(f, g):
        pass


    inspect.getfullargspec(foo)

    print(inspect.getfullargspec(foo))
