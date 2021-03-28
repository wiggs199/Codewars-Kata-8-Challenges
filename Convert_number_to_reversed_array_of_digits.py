'''

Convert number to reversed array of digits

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

348597 => [7,9,5,8,4,3]

Solution below:

'''


def digitize(n):

    numbers = list(map(int, str(n)))
    numbers.reverse()
    return numbers
