def bubble(num):
    n = len(num)
    for i in range(n-2,-1,-1):
        is_swap=False
        for j in range(0,i+1):
            if num[j] > num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]
                is_swap = True
    if is_swap==False:
        return num

num=[9,7,2,6,1,3,5]
print(bubble(num))