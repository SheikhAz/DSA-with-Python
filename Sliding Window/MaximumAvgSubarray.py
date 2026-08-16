nums = [1,12,-5,-6,50,3]
k = 4

def MaxAvg(nums,k):
    n = len(nums)
    sum = 0
    for i in range(0,k):
        sum += nums[i]

    maxSum = sum
    for i in range(k,n):
        sum -= nums[i-k]
        sum += nums[i]
        maxSum = max(maxSum,sum)

    return maxSum/k

print(MaxAvg(nums,k))