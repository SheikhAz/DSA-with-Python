n = [2,3,4,5,8,4,2,9,10,1,1]
m = [4, 5, 6, 7, 8,7]

result = []
hash_list = [0]*11
for num in n:
    hash_list[num] += 1

for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        result.append(hash_list[num])

print(result)