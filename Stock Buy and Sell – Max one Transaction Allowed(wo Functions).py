class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        minsofar=prices[0]
        for price in prices:
            if minsofar>price:
                minsofar=price
            elif res<price-minsofar:
                res=price-minsofar
        return res
        
