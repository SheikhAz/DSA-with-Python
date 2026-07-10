nums = [23,321,32,55,21,66,223]

def largest(nums):
    n = len(nums)
    largest = nums[0]
    for i in range(0,n):
        largest = max(largest , nums[i])
    return largest


print(largest(nums))