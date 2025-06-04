class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        positioner=1 #that pointer to the next adjusting postion which obey 2 element rule
        #i:::iterator of the array
        for i in range(1,len(nums)):
            if positioner==1 or nums[i]!=nums[positioner-2]:
                nums[positioner]=nums[i]
                positioner+=1
        return positioner
