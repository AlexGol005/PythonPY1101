def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i], iterable[i+1]


def task():
    for pair in pairwise("ABCDEFG"):
        print(pair)

def sum_path(coordinats: list):
    i = 1
    sum = 0
    while i < len(coordinats):
        otrez = round((((coordinats[i][0] - coordinats[i-1][0])**2) + ((coordinats[i][1] - coordinats[i-1][1])**2))**(1/2), 1)
        sum += otrez
        i = i + 1
    print(sum)

if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]
    sum_path(pts)