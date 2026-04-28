target = 20
result = []
for i in range(1 , target+1):
    if target%i==0:
        result.append(i)

print(result)