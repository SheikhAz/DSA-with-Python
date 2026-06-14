
def ispalindrome(s):
    l,r = 0, len(s)-1
    while r > l:
        while r > l and not s.isalnum():
            l += 1
        while r > l and not s.isalnum():
            r -=1
        
        if s[l].lower() != s[r].lower():
            return False
        
        l += 1
        r -= 1
    return True
s = "A man, a plan, a canal: Panama"
print(ispalindrome(s))



def validpalindrome(s):
    l , r = 0,len(s)-1
    def palindrome(l,r):
        while r > l:
            if s[l]!=s[r]:
                return False
            
            l += 1
            r -= 1
        return True

    while r > l:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return palindrome(l+1,r) or palindrome(l,r-1)
    return True

s = "abca"
print(validpalindrome(s))