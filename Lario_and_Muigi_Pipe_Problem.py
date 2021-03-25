'''
Issue
Looks like some hoodlum plumber and his brother has been running around and damaging your stages again.

The pipes connecting your level's stages together need to be fixed before you receive any more complaints. Each pipe should be connecting, since the levels ascend, you can assume every number in the sequence after the first index will be greater than the previous and that there will be no duplicates.

Task
Given the a list of numbers, return the list so that the values increment by 1 for each index up to the maximum value.

Example
Input: 1,3,5,6,7,8

Output: 1,2,3,4,5,6,7,8

FUNDAMENTALSLOOPSCONTROL FLOWBASIC LANGUAGE FEATURESLISTSDATA STRUCTURESOBJECTS

Sloution Below :

'''


def pipe_fix(nums):
    first_num = nums[0]
    last_num = nums[-1] + 1
    x = range(first_num, last_num)
    new_list = []
    for n in x:
        new_list.append(n)
    return new_list
