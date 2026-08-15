height = [1,8,6,2,5,4,8,3,7]

def maxArea(height):
    i=0
    j=len(height)-1
    maxarea = 0
    while j >= i:
        H = min(height[i],height[j])
        W = j - i
        area = H * W

        maxarea = max(maxarea,area)
        if height[j] > height[i]:
            i += 1
        else:
            j -= 1
    return maxarea

print(maxArea(height))