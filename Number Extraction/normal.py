nums = 83828382
result = []

while nums > 0:
    l_digit = nums % 10
    result.append(l_digit)
    nums = nums//10

print(result)