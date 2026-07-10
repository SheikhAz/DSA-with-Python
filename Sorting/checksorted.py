nums = [12,1,2,13,4,2,5]

def isSorted(nums):
    n = len(nums)
    for i in range(0,n-1):
        if nums[i] > nums[i+1]:
            return False
    return True


print(isSorted(nums))