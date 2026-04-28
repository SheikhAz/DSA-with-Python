n = 153
total = 0
p = len(str(n))

for i in str(n):
    total = total + (int(i)**p)

print(n == total)