
def access_examples():
    the_string = 'All the world’s a stage,\nAnd all the men and women merely players;'
    print(the_string[2], the_string[17], the_string[22], the_string[54], sep='|')
    # print(the_string[123])

    for char in the_string:
        print(char, end='|')
    print()

def slice_examples():
    the_string = 'asdfghjkl;'
    print(the_string[2:5], the_string[1: 8], the_string[4: 9])

    another_string = 'abcdefghijklmnopqrstuvwxyz0123456789'
    print(another_string[0: 0], another_string[0: 1], another_string[5: -5], another_string[-2: 2], sep='\n')
    start = ''
    stop = ''
    try:
        while True:
            start, stop = [int(x) for x in input('Enter start stop').split()]
            try:
                print('the array slice is: ', another_string[start: stop])
            except IndexError:
                print('the slice is out of bounds')
    except ValueError:
        print('broken out')

def slice_list():
    a_list = [1, 2, 3, 4, 5]
    print(a_list[3:5])  # [4, 5]
    print(a_list[3:])  # [4, 5]
    print(a_list[:2])  # [1, 2]

    the_list = ['a', 1, 'b', 2, 'c', 3]
    print(the_list[2:4])  # ['b', 2]
    print(the_list[1:6])  # [1, 'b', 2, 'c', 3]

    print(the_list[-3:-1])  # [2, 'c']
    print(the_list[-5:-2])  # [1, 'b', 2]
    print(the_list[-2:-5])  # []


def the_dangers_of_slice(n=0):
    import time
    import random

    if n == 0:
        n = int(input('Enter the number of times we go: '))
    s = ''
    for _ in range(n):
        s += 'a'
    start_time = time.time() * 1000
    new_strings = []
    for _ in range(n):
        start, stop = [random.randint(0, n), random.randint(0, n)]
        new_strings.append(s[start: stop])
    total_time = time.time() * 1000 - start_time
    print(total_time)


if __name__ == '__main__':
    # access_examples()
    # slice_examples()
    # slice_list()

    for n in [100, 1000, 10000, 100000, 1000000]:
        the_dangers_of_slice(n)
