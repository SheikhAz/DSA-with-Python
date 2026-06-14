s = "aaa"
def countSubstrings(s):
        res=0
        def countpali(s,l,r):
            res = 0
            while l >= 0 and r < len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            return res
        
        for i in range(len(s)):
            res += countpali(s,i,i)
            res += countpali(s,i,i+1)
        return res

print(countSubstrings(s))