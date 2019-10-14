import time

def check_if_integer(s):
    NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    NEGATIVE_SIGN = '-'
    split_string = s.strip.split()

    if len(split_string) == 2 and split_string[0] != NEGATIVE_SIGN:
        return False

    for c in split_string[-1]:
        if c not in NUMBERS:
            return False

    return True

BOARD_SIZE = 3

def check_board(board, x_move, y_move):
    if board[x_move][y_move] in ['x', 'o']:
        return False
    else:
        return True


def get_primes_slower(n):
    prime_list = [2]
    for x in range(3, n + 1):
        is_prime = True
        for i in range(2, x):
            if x % i == 0:
                is_prime = False
        if is_prime:
            prime_list.append(x)
    return prime_list


def pair_max(x, y):
    if x < y:
        return y
    else:
        return x


def is_prime(x):
    for i in range(2, x):
        if not x % i:
            return False
    return True


def is_prime_improved(x, prime_list):
    for p in prime_list:
        if not x % p:
            return False
    return True


def get_primes(n):
    prime_list = [2]
    for x in range(3, n + 1):
        if is_prime(x):
            prime_list.append(x)
    return prime_list


def get_primes_improved(n):
    prime_list = [2]
    for x in range(3, n + 1):
        if is_prime_improved(x, prime_list):
            prime_list.append(x)
    return prime_list


def calculate_volume(length, width, height):
    if length > 0 and width > 0 and height > 0:
        return length * width * height

    return 0


def check_tic_tac_toe(board):
    for first in range(BOARD_SIZE):
        if board[first][0] == 'x':
            check_row_for = 'x'
        elif board[first][0] == 'o':
            check_row_for ='o'
        else:
            check_row_for = ''

        if board[0][first] == 'x':
            check_col_for = 'x'
        elif board[0][first] == 'o':
            check_col_for ='o'
        else:
            check_col_for = ''
        if check_row_for:
            row_check = True
            for col in range(BOARD_SIZE):
                if board[first][col] != check_row_for:
                    pass


def is_palindrome(the_string):
    for i in range(len(the_string)):
        if the_string[i] != the_string[len(the_string) - 1 - i]:
            return False
    return True


if __name__ == '__main__':
    n = int(input('Enter n: '))
    while n != -1:
        t_0 = time.process_time()
        get_primes(n)
        t_stop = time.process_time()
        print(t_stop - t_0)

        t_0 = time.process_time()
        get_primes_improved(n)
        t_stop = time.process_time()
        print(t_stop - t_0)
        n = int(input('Enter n: '))

    s = input('enter palindrome: ')
    while s != 'quit':
        print(s, is_palindrome(s))
        s = input('enter palindrome: ')