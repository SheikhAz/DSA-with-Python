nums = 153
n = nums
total = 0
p = len(str(n))

while n > 0:
    m = n%10
    total = total + (m**p)
    n = n // 10
print(total == nums)