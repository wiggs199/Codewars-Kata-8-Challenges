'''

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

Solution below

'''


def move_zeros(array):
    remove_zero = [0]
    zero_count = array.count(0)
    filtered_list = []

    for num in array:
        if num not in remove_zero:
            filtered_list.append(num)

    return filtered_list + remove_zero * zero_count
