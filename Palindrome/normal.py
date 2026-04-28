nums = 84828
result = 0
while nums > 0 :
    l = nums%10
    result = (result * 10) + l
    nums = nums//10

if nums == result:
    print ('Yes, it is Palindrome')

else:
    print('No, it is not palindrome')