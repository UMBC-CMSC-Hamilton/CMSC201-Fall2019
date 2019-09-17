import random

if __name__ == '__main__':
    what_does_this_do = [i + 1 for i in range(10)]
    for i in range(len(what_does_this_do)):
        what_does_this_do[i] += 1
    print(what_does_this_do)

    the_list = [random.randint(0, 100) for _ in range(10)]
    print(the_list)
    for x in the_list:
        if x > 50:
            print(x, 'is bigger than 50')
            x *= 3
    print(the_list)

    for i in range(len(the_list)):
        if the_list[i] > 50:
            print(the_list[i], 'is bigger than 50')
            the_list[i] *= 2
    print(the_list)

fridge = ['eggs', 'cheese', 'lunch meat', 'green peppers', 'milk', 'avocados']
for thing in fridge:
    if thing == 'milk':
        print('we have milk')

if 'milk' in fridge:
    print('we have milk')