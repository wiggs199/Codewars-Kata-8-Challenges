'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.

'''
def generate_hashtag(s):
    #your code here
    
    hash = '#'
    group = s.split()
    new = [x.capitalize() for x in group]
    listToStr = ''.join(map(str,new))

    if listToStr == '' or len(s) > 140 :
        return False
    else:
        return hash + listToStr