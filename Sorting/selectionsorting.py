def selection(nums):
    n = len(nums)
    for i in range (0,n):
        mini = i
        for j in range(i+1,n):
            if nums[j] < nums[mini]:
                mini = j

        nums[i],nums[mini] = nums[mini],nums[i]
    return nums


nums = [9,3,2,4,5,4,3,1]
print(selection(nums))

