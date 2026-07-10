
nums = [23,321,32,55,21,66,223]

def secondlarge(nums):
    largest = float("-inf")
    s_largest = float("-inf")
    n = len(nums)
    for i in range (0,n):
        if nums[i] > largest:
            s_largest = largest
            largest = nums[i]
        elif nums[i] > s_largest and s_largest != largest:
            s_largest = nums[i]
    return s_largest


print(secondlarge(nums))