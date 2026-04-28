from math import *

nums = 9898
def countDigit(nums):
    return int(log10(nums) + 1)

print(countDigit(nums))