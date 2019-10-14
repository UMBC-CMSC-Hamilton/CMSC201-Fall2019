
def first_example():
    x = 3
    x += 17
    print('this is a function', x)


def square_me(x):
    print('x squared is', x ** 2)


def weird_function(the_string):
    if 'magic' in the_string.lower():
        print('There\'s some magic going on here.')
    if '2' in the_string or 'two' in the_string.lower():
        print('There\'s no such thing as two')


def take_the_square_root(number):
    current = 1
    previous = 0
    while abs(current - previous) > 1.0E-12:
        previous = current
        current = (1/2) * (previous + number / previous)
    return current


def pass_by_reference(the_list):
    if 'hello' in the_list:
        the_list.append('goodbye')


def count_a(the_string):
    count = 0
    for c in the_string:
        if c == 'a':
            count += 1
    return count


def count_2s(number):
    count = 0
    while not number % 2:
        number //= 2
        count += 1
    return count


CODES = [1859456453, 1824589548, 156185788, 15196857, 1234185496]
USER_NAMES = ['Joe', 'Rebecca', 'Adam', 'Barbara', 'Samantha']


def verify_user(name, code):
    for i in range(len(USER_NAMES)):
        if name == USER_NAMES[i] and int(code) == CODES[i]:
            return True
    return False


def log_in():
    user_name = input('Enter your name: ')
    user_code = input('Enter your code: ')
    for i in range(5):
        if verify_user(user_name, user_code):
            print('Access Granted')
            return True
        else:
            print('Invalid Code, Try Again')
            user_code = input('Enter your code: ')
    return False


if __name__ == '__main__':
    my_list = ['hello', 'robot', 'reference', 'value']
    pass_by_reference(my_list)
    print(my_list)

    x = 5
    y = square_me(x)
    z = take_the_square_root(x)
    print(x, y, z)



    #     while not log_in():
    #         print('Access Denied, Try Again')
    # print(count_a('this string may have some as in it or may not or whatever'))
    # print(count_2s(1024))
    # print(count_a('in this string, the letter eyh exists does not'))
    # print(count_2s(876))
    # first_example()
    # square_me(x)

    # sqrt_5 = take_the_square_root(5)
    # print(current, previous)

    # print(take_the_square_root(17))
    # print(sqrt_5)

