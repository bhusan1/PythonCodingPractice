"""
Create a program that asks the user for a number and then prints out 
a list of all the divisors of that number. (If you don’t know what a 
divisor is, it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""
def find_divisors():
    num = int(input("Enter a number, to find divisor: "))
    divisors = []
    while num%2 == 0:
        num = int(num / 2)
        if num >2:
            divisors.append(num)
    print(divisors)


find_divisors()