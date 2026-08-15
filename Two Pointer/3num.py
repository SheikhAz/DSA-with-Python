nums = [-1,0,1,2,-1,-4]

def threeNum(nums):
    result = set()
    n = len(nums)
    for i in range(n):
        my_set = set()
        for j in range(i+1,n):
            k = -(nums[i] + nums[j])
            if k in my_set:
                temp = [nums[i],nums[j],k]
                temp.sort()
                result.add(tuple(temp))
            my_set.add(nums[j])
    return [list(ans) for ans in result]

print(threeNum(nums))
