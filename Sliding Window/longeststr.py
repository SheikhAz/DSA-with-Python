s = "abcabcbb"

def Longstr(s):
    n = len(s)
    hashset = set()
    left = 0
    L = 0
    for right in range(n):
        while s[right] in hashset:
            hashset.remove(s[left])
            left += 1

        hashset.add(s[right])
        L = max(L,right - left +1)
    return L
print(Longstr(s))