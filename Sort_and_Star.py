'''

You will be given a vector of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

The returned value must be a string, and have "***" between each of its letters.

You should not remove or add elements from/to the array.

Solution below :

'''


def two_sort(array):
    # your code here
    array.sort()
    new_bit = array[0]
    new_string = str(new_bit)
    new_list = list(new_string)
    aces = [suit + "***" for suit in new_list[:-1]]
    str1 = ''.join(aces)
    return str1 + new_string[-1]
