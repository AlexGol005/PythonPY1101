import itertools
from string import ascii_lowercase, ascii_uppercase, digits
import random
def gen_password(n=8):
    while True:
        population = (ascii_lowercase + ascii_uppercase + digits)
        yield ''.join(random.sample(population, n))

if __name__ == "__main__":
    a = gen_password(10)
    for i in range(10):
        print(''.join(list(next(a))))