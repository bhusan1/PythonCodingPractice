"""
Given an array length 1 or more of ints, return the difference
between the largest and smallest values in the array. 
Note: the built-in min(v1, v2) and max(v1, v2) functions return 
the smaller or larger of two values.

big_diff([10, 3, 5, 6]) → 7
big_diff([7, 2, 10, 9]) → 8
big_diff([2, 10, 7, 2]) → 8
"""
def big_diff(nums):
    """min_value = nums[0]
    max_value = nums[0]
    for num in nums:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    return max_value-min_value
"""
    return max(nums)-min(nums)
    
print(big_diff([10,3,5,6]))
        