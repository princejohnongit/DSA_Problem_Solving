class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word
        res=''
        max_len=len(word)-numFriends+1
        for i in range(0,len(word)):
            temp=word[i:i+max_len]
            if temp>res:
                res=temp
        return res
