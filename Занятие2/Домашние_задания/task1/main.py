def geo_progress_generator(num):
    yield num
    b = num
    while True:
        num = b * num
        yield num


if __name__ == "__main__":
    geo_progress = geo_progress_generator(5)
    for _ in range(10):

        print(next(geo_progress))
