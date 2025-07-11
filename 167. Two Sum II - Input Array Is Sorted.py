class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end=1
        n=len(numbers)
        while end<n:
            add=numbers[start]+numbers[end]
            if add<target:
                end+=1
                start+=1
            elif add>target:
                start-=1
            else:
                return [start+1,end+1]
    
        
