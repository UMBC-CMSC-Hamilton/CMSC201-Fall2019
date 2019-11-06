import random
import time


def swap(a_list, i, j):
    temp = a_list[i]
    a_list[i] = a_list[j]
    a_list[j] = temp


def bubble_sort(the_list):
    for i in range(len(the_list)):
        for j in range(len(the_list) - 1):
            if the_list[j] > the_list[j + 1]:
                swap(the_list, j, j + 1)
    return the_list


def selection_sort(the_list):
    for i in range(len(the_list)):
        min_index = i
        for j in range(i + 1, len(the_list)):
            if the_list[min_index] > the_list[j]:
                min_index = j
        swap(the_list, i, min_index)
    return the_list


def insertion_sort(the_list):
    for i in range(1, len(the_list)):
        j = i
        while j > 0 and the_list[j - 1] > the_list[j]:
            swap(the_list, j - 1, j)
            j -= 1

    return the_list


def merge_lists(first_list, second_list):
    first_index = 0
    second_index = 0
    merged_list = []
    while first_index < len(first_list) and second_index < len(second_list):
        if first_list[first_index] < second_list[second_index]:
            merged_list.append(first_list[first_index])
            first_index += 1
        else:
            merged_list.append(second_list[second_index])
            second_index += 1

    for i in range(first_index, len(first_list)):
        merged_list.append(first_list[i])

    for j in range(second_index, len(second_list)):
        merged_list.append(second_list[j])

    return merged_list


def merge_sort(the_list):
    half_length = len(the_list) // 2
    if len(the_list) >= 2:
        return merge_lists(merge_sort(the_list[0: half_length]), merge_sort(the_list[half_length:]))
    else:
        return the_list


def quick_sort(the_list):
    if len(the_list) >= 2:
        pivot = the_list[0]
        less_list = []
        equal_list = []
        greater_list = []

        # this is called the partition step
        for x in the_list:
            if x < pivot:
                less_list.append(x)
            elif x == pivot:
                equal_list.append(x)
            else:
                greater_list.append(x)
        # this is the recursive step
        return quick_sort(less_list) + equal_list + quick_sort(greater_list)
    else:
        return the_list  # if the list is empty, or just as one value, consider it sorted


def validate(sort_algorithm):
    num_elements = int(input('How many elements do you want in each list? '))
    num_tests = int(input('How many tests do you want to run? '))
    for _ in range(num_tests):
        test_list = [random.randint(0, 100) for _ in range(num_elements)]
        if sort_algorithm(test_list) == sorted(test_list):
            print(True)
            print(test_list)
        else:
            print(False)
            print(sort_algorithm(test_list))
            print(sorted(test_list))


def time_test(sort1, sort2):
    num_tests = int(input('How many tests do you want to run? '))
    num_elements = int(input('How many elements do you want in each list? '))
    for i in range(num_tests):
        print('Test', i + 1)
        test_list = [random.randint(0, 100) for _ in range(num_elements)]
        copy_1 = list(test_list)
        copy_2 = list(test_list)
        print('\tSort 1 starting')
        time_start = time.perf_counter()
        sort1(copy_1)
        print('\tSort 1 completed in', time.perf_counter() - time_start)
        time_start = time.perf_counter()
        print('\tSort 2 starting')
        sort2(copy_2)
        print('\tSort 2 completed in', time.perf_counter() - time_start)


if __name__ == '__main__':
    # validate(bubble_sort)
    # validate(insertion_sort)
    # validate(selection_sort)
    time_test(merge_sort, quick_sort)
    time_test(insertion_sort, quick_sort)