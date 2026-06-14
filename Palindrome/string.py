# Solve by using Recursion

n = 'nitin'
num = n
def pali(n,L,R):
    if L>=R:
        return
    if n[L] == n[R]:
        pali(n,L+1,R-1)
    else:
        return "Not a palindrome"
    
    return "It is Palindrome"

print(pali(num,0,len(n)-1))

# Solve using Loop

def paliloop(n,L,R):
    while R >= L:
        if n[L] == n[R]:
            L+=1
            R-=1
        else:
            return "It is not a palindrome"
        
    return 'it is Palindrome'

print(paliloop(n,0,len(n)-1))