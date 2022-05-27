"""
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list 
that are less than 5.
"""

def less10(nums):
    new_list = []
    for num in nums:
        if num < 5:
            new_list.append(num) 
    return new_list

print(less10([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]))