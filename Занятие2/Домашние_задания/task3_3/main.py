import inspect

def arg_type_int(fn):
    def wrapper(*args, **kwargs):
        a = inspect.getfullargspec(fn)
        gen = (_ for _ in a)
        if not isinstance(fn, int):
            raise TypeError("Объект <название или номер позиционного аргумента> <значение аргумента> не является итерируемым")
        result = fn(arg)
    return wrapper

if __name__ == "__main__":
    @arg_type_int
    def a(n):
        print(n)


    def foo(f, g):
        pass


    inspect.getfullargspec(foo)

    print(inspect.getfullargspec(foo))
