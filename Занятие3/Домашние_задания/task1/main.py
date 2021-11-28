f1 = '1.txt'
f2 = '2.txt'
c = '9876543210'
if __name__ == "__main__":
    with open(f1, 'r') as f1:
        for line in f1:
            a = line
    with open(f2, 'r') as f2:
        for line in f2:
            b = line
    list_ = [i for i in (a + b) if i in c]
    print(list_)

