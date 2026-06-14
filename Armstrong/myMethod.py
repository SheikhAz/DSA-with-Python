n = 153
total = 0
p = len(str(n))

for i in str(n):
    total = total + (int(i)**p)

print(n == total)


number = 1234
total = 0
p = len(str(number))

for i in str(number):
    total = total + int(i)**p

print(number == total)
print(total)