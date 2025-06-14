class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref=strs[0]
        pref_len=len(pref)
        #assume the pattern to be the first string
        for s in strs[1:]:
            #check for other strings
            while pref!=s[0:pref_len]:
                #if the pattern is not as 
                # same as the s string then reudce size
                pref_len-=1
                if pref_len==0:
                    return ""
                #update the ground truth coz it doesn't match
                pref=pref[0:pref_len] 
        return pref


        
