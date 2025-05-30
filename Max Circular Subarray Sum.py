class Solution:
    def circularSubarraySum(self, arr):
        
    # code here
        n=len(arr)
        #for non-wrapping
        global_max=arr[0]
        local_max=0
        
        #for wrapping
        total_sum=0
        global_min=arr[0]
        local_min=0
        
        for i in range(n):
            local_max=max(arr[i]+local_max,arr[i])
            global_max=max(local_max,global_max)
            
            local_min=min(local_min+arr[i],arr[i])
            global_min=min(local_min,global_min)
            total_sum=total_sum+arr[i]
        
        normal_sum=global_max    #possible linear max-sum subarray
        circular_sum=total_sum-global_min # possible circular max-sum subarry(wrapping)
        
        if total_sum==global_min:
            return normal_sum
        
        return max(normal_sum,circular_sum)
        
    
