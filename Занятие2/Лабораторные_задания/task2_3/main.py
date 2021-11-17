def pow_gen(base: int):
    ...  # TODO записать функцию-генератор
    i = 0

    while True:
        num = base ** i
        yield num
        i += 1

if __name__ == "__main__":
    pow_numbers = pow_gen(5)

    for _ in range(10):
        print(next(pow_numbers))
