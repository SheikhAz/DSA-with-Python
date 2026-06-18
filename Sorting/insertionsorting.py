def insertion(num):
    n = len(num)
    for i in range(1,n):
        key = num[i]
        j = i -1
        while  j >= 0 and num[j] > key:
            num[j+1] = num[j]
            j -=1
        num[j+1] = key
    return num

num = [9,3,2,1,8,6]
print(insertion(num))