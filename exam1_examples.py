def debugging_code():
    TTT_SIZE = 3
    tic_tac_toe_board = []
    for i in range(TTT_SIZE):
        tic_tac_toe_board.append([])
        for j in range(TTT_SIZE):
            tic_tac_toe_board.append(0)

    print(tic_tac_toe_board)


def lets_debug_again():
    # x is a list of numbers starting with 12
    x = 12
    s = input('Enter a number (quit to quit): ')
    while s != 'quit':
        x.append(int(s))

    for i in x:
        i **= 2

    # x will contain the squared values.
    print(x)

def what_does_this_button_do():
    s = 'this_is_a_long_string'

    for i in range(1, 17, 3):
        print(s[i])

    L = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    for i in range(17):
        print(L[(2 * i + 1) % 4][(5*i + 2) % 4])


# debugging_code()
what_does_this_button_do()
