target= 20 
result = []

for i in range(1,target//2+1):
    if target%i == 0:
        result.append(i)

result.append(target)
print(result)