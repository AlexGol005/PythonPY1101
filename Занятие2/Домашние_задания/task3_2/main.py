


def arg_type_int(fn):
    def wrapper(*args, **kwargs):

        if not isinstance(*args, int):
            raise TypeError(f"аргументы {fn} должен быть int")
        result = fn(*args, **kwargs)
    return wrapper

if __name__ == "__main__":
    @arg_type_int
    def a(n):
        print(n)


    a(2)
