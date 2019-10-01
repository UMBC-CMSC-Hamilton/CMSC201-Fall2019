the_list = [5, 2, 17, 8, 3, 189, 2, 18, 172, 1, 23, 1, 2, 34]

if __name__ == '__main__':
    selection = int(input('Select Problem 1, 2, 3: '))
    if selection == 1:
        '''
            Here is the first solution
        '''
        for i in range(len(the_list)):
            # find the minimum index
            current_index = i
            for j in range(i, len(the_list)):
                if the_list[current_index] > the_list[j]:
                    current_index = j
            # swap out the elements
            temp = the_list[current_index]
            the_list[current_index] = the_list[i]
            the_list[i] = temp
        # should be sorted now
        print(the_list)
        '''
            Here ends the first solution
        '''
    elif selection == 2:
        '''
            Here is the second solution
            
            This is a hard problem
        '''
        the_string = input('Enter the string: ')
        substring = input('Enter the substring to replace: ')
        replace_string = input('Enter the string to replace with: ')
        i = 0
        while substring in the_string and i < len(the_string):
            # find the starting index where the substring is
            index = 0
            while index < len(substring) and i + index < len(the_string) and the_string[i + index] == substring[index]:
                index += 1
            # if the index is the substring length then we know that we've found a complete substring so replace it using slices
            if index == len(substring):
                # the slice will be from 0 to i, so from 0 to the start of the substring minus one.
                # use string concatenation to put it together with the replace string
                # finally add the rest of the string back on and set it to the_string again.
                # note that we could have left the last len(the_string) out, since it is implicit
                #           the_string[i + len(substring):]
                the_string = the_string[0:i] + replace_string + the_string[i + len(substring): len(the_string)]
                # add length of the replace string to the position to move past the string replacement
                i += len(replace_string)
            else:
                # if its not a substring, then add one
                i += 1
        print(the_string)
    elif selection == 3:
        the_sum = 0
        min_value = the_list[0]
        max_value = the_list[0]
        for x in the_list:
            the_sum += x
            if min_value > x:
                min_value = x
            if max_value < x:
                max_value = x
        min_sum = the_sum - max_value
        max_sum = the_sum - min_value

        print('The minimum sum we can compute is', min_sum)
        print('The maximum sum we can compute is', max_sum)



    else:
        print('you have made an invalid selection')
