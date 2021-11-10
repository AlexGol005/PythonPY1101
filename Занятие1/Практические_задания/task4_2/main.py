from itertools import count


#def task():
    #iterator_numbers = count(1, 1)
    #numbers = [i ** 2 for i in iterator_numbers if i % 2 == 0]  # TODO заменить на map и filter бесконечный список

    #for num in numbers:  # TODO напечатать первые 10 чисел
        #print(num)  # TODO с помощью next получать следующий элемент от итератора

def task():
    iterator_numbers = count(1, 1)
    numbers = map(lambda x: x**2,
              filter(lambda x: x % 2 == 0, iterator_numbers))
    for _ in range(10):  # TODO напечатать первые 10 чисел
        print(next(numbers))

if __name__ == "__main__":
    task()
