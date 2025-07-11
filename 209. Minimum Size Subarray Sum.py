class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len=float("inf")
        left=0
        cur_sum=0
        for right in range(len(nums)):
            cur_sum+=nums[right] #chumma add the right elements 

            while cur_sum>=target: # based on the sum
                if right-left+1<min_len: #based on the array leng
                    min_len=right-left+1 #update length
                cur_sum-=nums[left] #chumma subs the left element
                left+=1 #chumma update left
        return min_len if min_len != float("inf") else 0 #return only if there is an updation
        
