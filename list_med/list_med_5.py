## confusing
"""
Return the sum of the numbers in the array, except ignore 
sections of numbers starting with a 6 and extending to the 
next 7 (every 6 will be followed by at least one 7). Return 0 
for no numbers.

sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
"""
def sum67(nums):
    count = 0
    blocked = False

    for num in nums:
        if num == 6:
            blocked = True
            continue
        if num == 7 and blocked:
            blocked = False
            continue
        if not blocked:
            count += num
    return count

print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))