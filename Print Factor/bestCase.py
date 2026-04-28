from math import sqrt

target = 20
result = []
for i in range(1,int(sqrt(target))+1):
    if target%i==0:
        result.append(i)
        if target//i!=i:
            result.append(target//i)

sorted_result = sorted(result)
print(sorted_result)