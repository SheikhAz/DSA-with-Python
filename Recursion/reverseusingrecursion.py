# By using Number.

n = [1,4,6,3,5,8,9]
def reversenum(n,L,R):
    if L >= R:
        return
    
    n[L],n[R]=n[R],n[L]
    reversenum(n,L+1,R-1)

reversenum(n,3,5)
print(n)

# By using Character

def reversech(n,L,R):
    if L >= R:
        return
    n[L],n[R] = n[R],n[L]
    reversech(n,L+1,R-1)

n=["a","d","a","t","t","t"]
reversech(n,0,len(n)-1)
print(n)