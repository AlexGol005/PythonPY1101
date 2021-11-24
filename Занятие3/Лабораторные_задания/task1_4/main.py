INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, 'r') as f1:
        with open(OUTPUT_FILE, 'w') as f2:
            for i in map(str.upper, f1):
                f2.write(i)








    ...  # TODO перезаписать содержимое одного файла в другой


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
