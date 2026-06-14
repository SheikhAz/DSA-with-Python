from math import *

nums = 46262464
def countDigit(nums):
    return int(log10(nums) + 1)

print(countDigit(nums))


number = 122123
count = 0
for i in str(number):
    count = count + 1

print(count)