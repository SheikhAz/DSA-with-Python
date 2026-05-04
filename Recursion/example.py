# count = 0
# def name():
#     global count
#     if count == 4:
#         return
#     count += 1
#     name()
#     print('hello Sheikh')
        
# name()

# * Head Recursion

# def fun(x,n):
#     if n==0:
#         return
#     print(x)
#     fun(x,n-1)

# fun(15,5)

# * Backtracking (Tail Recursion) N to 1

# def count(i,N):
#     if i > N:
#         return
#     count(i+1,N)
#     print(i)

# count(1,7)

# * Backtracking (Tail Recursion) 1 to N

def count(N):
    if N==0:
        return
    count(N-1)
    print(N)

count(5)

