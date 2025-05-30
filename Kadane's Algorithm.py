class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        max_end=arr[0]
        res=arr[0]
        for i in range(1,len(arr)):
            max_end=max(max_end+arr[i],arr[i])
            res=max(res,max_end)
        return res
            
