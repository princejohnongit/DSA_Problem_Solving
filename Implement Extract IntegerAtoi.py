#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        sign=1
        idx=0
        res=0
        symbol=['-','+']
        n=len(s)
        
        while idx<n and s[idx]==' ':
            idx+=1
            
        if s[idx] in symbol:
            if s[idx]=='-':
                sign=-1
            idx+=1
            
        while idx<n and '0'<=s[idx]<='9':
            res=res*10+(ord(s[idx])-ord('0'))
            if res>(2**31-1):
                return sign*(2**31-1) if sign==1 else -2**31
            idx+=1
            
        return sign*res
