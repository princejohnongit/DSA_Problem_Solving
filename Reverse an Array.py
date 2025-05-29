class Solution:
    def reverseArray(self, arr):
        start=0
        end=len(arr)
        for i in range(end//2):
            temp=arr[start]
            arr[start]=arr[end-1]
            arr[end-1]=temp
            start+=1
            end-=1
        
