class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n=len(arr)
        res=[]
        vote={}
        for i in arr:
            vote[i]=vote.get(i,0)+1
        
        for ele,cnt in vote.items():
            if cnt>n//3: res.append(ele)
        
        res.sort()
        
        return res
