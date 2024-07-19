import math

def findGCD(nums):
    smallest = min(nums)
    largest = max(nums)
    return math.gcd(smallest, largest)


print(findGCD([2, 5, 6, 9, 10]))  
print(findGCD([7, 5, 6, 8, 3]))  
print(findGCD([3, 3]))           

