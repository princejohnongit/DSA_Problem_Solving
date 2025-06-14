class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
        for i in s[::-1]:
            print(i,'xxx')
            if i==' ':          
                if count!=0:
                    return count
                continue
            count+=1
        return count
