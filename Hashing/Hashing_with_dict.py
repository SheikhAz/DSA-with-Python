n = [2,3,4,5,8,4,2,9,10,1,1]
m = [4, 5, 6, 7, 8,7]

f_map = {}
result = {}
for i in range(0,len(n)):
    if n[i] in f_map:
        f_map[n[i]] += 1
    else:
        f_map[n[i]] = 1

for i in range(0,len(m)):
    if m[i] in f_map:
        print(m[i],"frequency is =",f_map[m[i]]) 