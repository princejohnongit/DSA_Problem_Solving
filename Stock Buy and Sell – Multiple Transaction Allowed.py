from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code 
        res=0
        n=len(prices)
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                res=res+prices[i]-prices[i-1]
        return res
            
            
