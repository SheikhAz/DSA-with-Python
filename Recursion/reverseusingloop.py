def reversenum(n,L,R):
    while L <= R:
        n[L],n[R] = n[R],n[L]
        L+=1
        R-=1

n = [1,4,6,3,5,8,9]
reversenum(n,0,len(n)-1)
print(n)

# similar for character