from string import ascii_lowercase, ascii_uppercase, digits
import random
def gen_password(k):
    population = [x for x in ascii_lowercase + ascii_uppercase + digits]
    return random.sample(population, k)

if __name__ == "__main__":
    print(ascii_lowercase)
    print(ascii_uppercase)
    print(digits)
    print(''.join(gen_password(8)))