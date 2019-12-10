
def sort_alphabetically(file_name):
    with open(file_name) as the_file:
        lines = the_file.readlines()
        
        list_sorted = False
        while not list_sorted:
            list_sorted = True
            for i in range(len(lines) - 1):
                if lines[i].lower() > lines[i + 1].lower():
                    temp = lines[i]
                    lines[i] = lines[i + 1]
                    lines[i + 1] = temp
                    list_sorted = False
        return lines


def selection_sort(the_list):
    for i in range(len(the_list)):
        min_index = i
        for j in range(i, len(the_list)):
            if the_list[min_index] > the_list[j]:
                min_index = j
        temp = the_list[min_index]
        the_list[min_index] = the_list[i]
        the_list[i] = temp

    return the_list


# Bubble sort is Omega(n) and O(n^2)
# selection sort is Omega(n^2) and O(n^2) so overall Theta(n^2)
# Quick Sort is Omega(n lg(n)) and O(n^2)
# linear search is Omega(1) and O(n)
# binary search is Omega(1) and O(lg(n))

def divides_evenly(n, x):
    if n % x != 0 or n == 0:
        return 0
    else:
        return 1 + divides_evenly(n // x, x)
        

if __name__ == '__main__':
    the_dictionary = {}
    the_dictionary['hello'] = 3
    print(the_dictionary.get('robots'))
    the_dictionary['robots'] = 17
    the_dictionary['keys'] = 32
    the_dictionary['glue'] = 654
    the_dictionary['battle bottle'] = 9
    the_dictionary['bees?'] = 37

    print(the_dictionary['glue'])
    print(the_dictionary.keys())
    print(the_dictionary.values())

    # number of times that x divides n, evenly
    # 127, 5 -> 0
    # 125, 5 -> 3
    # 24 (8 * 3), 2 -> 3

    print(sort_alphabetically('blah.txt'))
