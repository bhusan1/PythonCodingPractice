##MediumString
"""
Given a string and a non-negative int n, return a larger string that 
is n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""
def string_times(str, n):
    largeStr = ""
    for i in range(n):
        largeStr = largeStr + str
    return largeStr

print(string_times("Yo", 5))
