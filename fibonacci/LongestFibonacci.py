def longestSubarray(nums):
        n = len(nums)
        hash=[0]*n
        for i in range(2,n):
            if nums[i-1]+nums[i-2] == nums[i]:
                hash[i] = hash[i-1]+1
        return max(hash)+2
 
nums = [1,1,1,1,2,3,5,1]
print(longestSubarray(nums))