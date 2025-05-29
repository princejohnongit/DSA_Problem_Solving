#User function Template for python3

class Solution:
    def pushZerosToEnd(self,arr):
        #zero_position_pointer: zpp
        #zpp is where the zero is currently assumed to be, a trash position to switch\
        #when you see a non-zero element swap it with zpp, make the next position to 
        #be the trash pointer aka zpp
        zpp=0
        for i in range(len(arr)):
            if arr[i]!=0:
                arr[i],arr[zpp]=arr[zpp],arr[i]
                zpp+=1
                
