'''
Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. 

All words must have their first letter capitalized without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord

Solution Below:

'''


def camel_case(string):
    new_list = string.split()
    arr = [word.capitalize() for word in new_list]
    empty_string = " "
    new_str = empty_string.join(arr)
    return new_str.replace(" ", "")
