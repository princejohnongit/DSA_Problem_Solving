class Solution:
    def reverse(self,nums,start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
        
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n #2
        ##print(nums[-k:n]+nums[:-k])
        #return'''
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
        
