class Solution:
    def getSecondLargest(self, arr):
        largest=-1
        second_largest=-1
        for i in arr:
            if i>largest:
                second_largest=largest
                largest=i
                
            if i>second_largest and i<largest:
                second_largest=i
        return second_largest
