#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def log_maker(self,s):
        log={}
        for i in range(len(s)):
            if s[i] in log:
                log[s[i]]+=1
            else:
                log[s[i]]=1
        return log
    def areAnagrams(self, s1, s2):
        log1=self.log_maker(s1)
        log2=self.log_maker(s2)
        
        if log1!=log2:
            return False
        else:
            return True
        
