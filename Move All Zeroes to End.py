#User function Template for python3

class Solution:
    def pushZerosToEnd(self,arr):
        z=0
        l=len(arr)
        for i in range(l):
            if arr[i]==0:
                z+=1
            else:
                arr[i-z]=arr[i]
                if z!=0: arr[i]=0
        return arr
        
