#User function Template for python3

class Solution:
    def pushZerosToEnd(self,arr):
        #zero_position_pointer: zpp
        zpp=0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[i],arr[zpp]=arr[zpp],arr[i]
                zpp+=1
                
