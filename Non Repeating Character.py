class Solution:
    def nonRepeatingChar(self,s):
        #code here
        MAX_CHAR=26
        visited=[-1]*MAX_CHAR
        
        #loop to create a visited index for each alphabet
        #the index is stored, if one occurence
        for i in range(len(s)):
            index=ord(s[i])-ord('a')
            if visited[index]==-1:
                visited[index]=i
            else:
                visited[index]=-2
       
        idx=-1 #index for calculating the smallest value
        
        #loop to return the index of the alphabet which has the lowest index of single 
        #occurnece
        for i in range(MAX_CHAR):
            if visited[i]>=0 and (idx==-1 or visited[i]<visited[idx]):
                idx=i
        
        #return the alphabet in the string
        #---which has the lowest index in the string in the visited
        return '$' if idx==-1 else s[visited[idx]]
            
        
    
    
