#User function Template for python3
class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self,arr):
        n=len(arr)
        global_max=arr[0]
        local_min=arr[0]
        local_max=arr[0]
        for i in range(1,n):
            temp=max(arr[i],local_min*arr[i],local_max*arr[i])
            local_min=min(arr[i],local_min*arr[i],local_max*arr[i])
            local_max=temp
            
            global_max=max(global_max,local_max)
        return global_max
