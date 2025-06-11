class Solution:
    # Function to find the majority elements in the array
    '''
    Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
    there will only be two elements in that case if there is sich elements
    '''
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
