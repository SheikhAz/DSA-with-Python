nums= [3,1,2,3,4,53,9,4,4]

def mergesort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = mergesort(nums[:mid])
    right = mergesort(nums[mid:])
    return mergearr(left,right)



def mergearr(left,right):
    result = []
    m ,n = len(left),len(right)
    i,j = 0,0
    while i < n and j < m:
        if right[i] <= left[j]:
            result.append(right[i])
            i += 1
        else:
            result.append(left[j])
            j += 1
    if i < n:
        while i < n:
            result.append(right[i])
            i += 1
    if j < m:
        while j < m:
            result.append(left[j])
            j += 1

    return result

print(mergesort(nums))