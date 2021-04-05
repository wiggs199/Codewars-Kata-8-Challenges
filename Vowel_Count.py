'''

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

Solution Below:

'''


def getCount(inputStr):
    num_vowels = 0
    # your code here
    vowels = 'a', 'e', 'i', 'o', 'u'
    for i in vowels:
        for b in inputStr:
            if i == b:
                num_vowels += 1

    return num_vowels
