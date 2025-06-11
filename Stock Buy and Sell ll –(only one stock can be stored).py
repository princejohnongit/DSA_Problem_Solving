class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxo=0
        minso=prices[0]
        for i in range(1,len(prices)):
            if prices[i]>minso:
                maxo=maxo+prices[i]-minso
            minso=prices[i]

        return maxo
