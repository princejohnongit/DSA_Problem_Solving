class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        cnt=0
        candles=[1]*n
        for i in range(1,n):
            #this loops give candles to the next kid in clockwise
            #first kid is ignored'
            #check the right kid supermacy
            if ratings[i-1]<ratings[i]:
                candles[i]=candles[i-1]+1 #one more than next left kid
        for i in range(n-1,0,-1):
            #this loops comes from rear end to the left.
            #ignore the candle of the last kid
            #check th supermacy of the left kid
            if ratings[i-1]>ratings[i]:
                #is already greater or 1 plus right
                candles[i-1]=max(candles[i-1],candles[i]+1)
            cnt+=candles[i]
        return cnt+candles[0]

            
        
