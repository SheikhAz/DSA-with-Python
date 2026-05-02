x = 4673
nums = x
result = 0
while nums > 0:
    l = nums % 10
    result = (result*10) + l
    nums = nums//10

print(nums == result) 