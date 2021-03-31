'''

Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)

Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

Examples

 123 ->  321
-456 -> -654
1000 ->    1

Solution Below :

'''


def reverse_number(n):
    if n < 0:
        new_str = str(n)
        next_str = new_str.replace('-', '')
        next_string = next_str[::-1]
        conv_str = '-' + next_string
        return int(conv_str)
    else:
        new_str = str(n)
        int_str = new_str[::-1]
        return int(int_str)
