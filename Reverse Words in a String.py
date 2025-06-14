class Solution:
    def reverseWords(self, s: str) -> str:
        sent=s.split()
        print(sent)
        return ' '.join(sent[::-1])


#---------------------------------------------------------------------------------------------------------------------
class Solution:
    def reverseWords(self, s: str) -> str:
        sent=s.split()
        n=len(sent)
        l=0
        r=n-1
        while l<=r:
            sent[l],sent[r]=sent[r],sent[l]
            l+=1
            r-=1
        return ' '.join(sent)
        
