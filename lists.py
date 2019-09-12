mixed_list = ['robot', 33, 12, 3.13, 17, 'Shakespeare', None]
some_other_list = [1, 2, 4, 8, 16, 32, 64, 128, 256]

# L = [] or L = list()
L = []
if L:
    print('Empty List is True')
else:
    print('Empty List is False')
#               0     1   2   3   4    5
access_list = [17, 1729, 14, 25, 81, 343]

list_of_lists = [3, [1, 2], 17, 'yep', []]

# print(access_list[6])

print(access_list)
print(access_list[1], access_list[3], access_list[5])
access_list[2] = 'changed'
access_list[5] = 1594848
print(access_list)
access_list.append("new thing")
print(access_list)
access_list.append("another thing")
print(access_list)
access_list.append(17)
print(access_list)


the_list = []
def do_something_to(x):
    return x


for value in the_list:
    do_something_to(value)

loop_list = [1, 5, 10, 12, 17, 19, 31, 33, 47, 52]
for value in loop_list:
    print(value, end=' ')

word_list = ['trap', 'squalid', 'stamp', 'injure', 'plane', 'kindhearted', 'treat', 'bomb', 'scold', 'wrap', 'preach', 'influence', 'like', 'arm', 'damaging', 'yam', 'authority', 'loud', 'present', 'wren']
for word in word_list:
    if 'a' in word:
        print('The word', word, 'has an a in it.')

for x in range(10):
    do_something_to(x)

for x in range(2, 5):
    print(x)

for y in range(17, 101):
    print(y)

print(len(the_list))
print(len(some_other_list))

for i in range(len(the_list)):
    print(the_list[i])
