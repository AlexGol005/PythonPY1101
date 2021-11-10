if __name__ == "__main__":
    list_ = ['1', '2', '3']
    values = [i for i in list_]
    indexes = list(range(len(list_)))
    for _ in zip(indexes, values):
        print(_)
    print(dict(enumerate(list_)))
