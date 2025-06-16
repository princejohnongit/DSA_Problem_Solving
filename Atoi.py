class Solution:
    def myAtoi(self, s: str) -> int:
        res=0
        INT_MAX=2**31-1
        INT_MIN=-2**31
        i=0
        n=len(s)
        if n==0: return 0
        while i<n and s[i]==' ':
            i+=1
        if i==n: return 0
        sign=1
        symbols=['-','+']
        if s[i] in symbols:
            if s[i]=='-':
                sign=-1
            i+=1
        while i<n and s[i].isdigit():
            digit=int(s[i])
            if res>(INT_MAX-digit)//10:
                return INT_MAX if sign==1 else INT_MIN
            res=res*10+digit
            i+=1
        return res*sign
