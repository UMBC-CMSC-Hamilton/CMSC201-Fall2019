def test_find_replace_eat():
    """
    :return: True if tests are passed else False
    """
    tests_passed = True

    # let's test if everything is empty strings
    if find_replace_eat('', '', '', '') != '':
        print('Null Test Failed')
        tests_passed = False



def find_replace_eat(the_string, replace_str, replace_with, eat_string):
    """
    :param the_string: the string to be parsed
    :param replace_str: if this string is found, we replace it with the replace-with argument
    :param replace_with: use this to replace any string
    :param eat_string: if this substring is found, delete it
    :return: a new string after modification.
    """
    i = 0
    new_string = ''
    while i < len(the_string):
        if the_string[i: i + len(replace_str)] == replace_str: # blah
            new_string += replace_with
        elif the_string[i: i + len(eat_string)] == eat_string:
            new_string = ''
        else:
            new_string += the_string[i]
        i += 1

    return new_string


def num_times(number):
    count = 0
    while number // 3:
        count += 1
        number //= 3

    return count

if __name__ == '__main__':
