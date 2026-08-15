height = [0,1,0,2,1,0,1,3,2,1,2,1]

def tappingwater(height):
    sum = 0
    l = len(height)
    maxleft = [0] * l
    maxright = [0] * l

    maxleft[0] = height[0]
    for i in range (1 ,l):
        maxleft[i] = max(maxleft[i-1],height[i])

    maxright[-1] = height[-1]
    for i in range (l-2,-1,-1):
        maxright[i] = max(maxright[i+1],height[i])

    for i in range(len(height)):
        H = min(maxleft[i],maxright[i]) - height[i]
        sum += H

    return sum

print(tappingwater(height))