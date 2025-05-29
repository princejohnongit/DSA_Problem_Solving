#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here(
        n = len(arr)
        for i in range(n):
            while 1<=arr[i]<=n and arr[i]!=arr[arr[i]-1]: 
                #in range
                #not found in ints correct postion
                
                arr[arr[i]-1],arr[i]=arr[arr[i]-1],arr[i]
                
        
        for i in range(1,n+1):
            if arr[i-1]!=i:
                return i
        return n+1
        
        
