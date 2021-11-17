def positive_check(fn):
    def wrapper(arg):
        # TODO написать проверку положительности аргумента arg
        if arg > 0:
            result = fn(arg)
        else:
            raise ValueError("Аргумент функции не является положительным числом")
        return result

    return wrapper




# TODO задекорировать функцию

@positive_check
def some_func(num: int):
    ...


if __name__ == "__main__":
    some_func(5)  # всё хорошо

    some_func(-5)  # должна быть вызвана ошибка ValueError

    # some_func = other_decorator(some_func)