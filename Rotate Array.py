#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. aka left
    def rotateArr(self, arr, d):
        n=len(arr)
        d%=n
        self.reverse(arr,0,d-1)
        self.reverse(arr,d,n-1)
        self.reverse(arr,0,n-1)
    def reverse(self,arr,start,end):
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
