def num_evens_iterative(the_number):
    count = 0
    while the_number != 0:
        if the_number % 2 == 1:
            count += 1
        the_number //= 2
    return count


def num_evens(the_number):
    if the_number > 0:
        if the_number % 2 == 0:
            return num_evens(the_number // 2)
        else:
            return 1 + num_evens(the_number // 2)
    return 0


def test_num_evens():
    x = int(input('Enter number! '))
    while x != -1:
        print(num_evens(x))
        print(num_evens_iterative(x))
        x = int(input('Enter number! '))


CONSONANTS = 'bcdfghjklmnpqrstvwxyz'


def recursive_enlolination(the_string, previous):
    """
    :param the_string: the current string
    :param previous: the letter previous, start out as empty string
    :return: the enlolinated string
    """
    if the_string:
        if (not previous or previous.lower() in CONSONANTS) and the_string[0].lower() not in CONSONANTS:
            print('case 1', the_string, previous)
            return 'ol' + the_string[0] + recursive_enlolination(the_string[1:], the_string[0])
        else:
            print('case 2', the_string, previous)
            return the_string[0] + recursive_enlolination(the_string[1:], the_string[0])
    else:
        if previous and previous in CONSONANTS:
            return 'ol'
        else:
            return ''


def test_recursive_enlolination():
    s = input('enter words: ')
    while s.lower() != 'quit':
        print(recursive_enlolination(s, ''))
        s = input('enter words: ')


def reversing_a_list(the_list):
    if the_list:
        return reversing_a_list(the_list[1:]) + [the_list[0]]
    else:
        return []


def test_list_reversal():
    """
    Let's write a test function
    """
    pass


if __name__ == '__main__':
    test_num = int(input('enter test 1, 2, 3: '))
    if test_num == 1:
        test_num_evens()
    elif test_num == 2:
        test_list_reversal()
    else:
        test_recursive_enlolination()
