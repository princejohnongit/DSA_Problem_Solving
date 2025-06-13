class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        leftover_gas=0 
        '''
        leftover gas at the positon at i after
        subtracting to check
        the gas filled at i is enought to travel from i -> i+1 
        here the prev leftover are also used
        this is possible only due "Unique Solution"
        '''
        start=0   
        for i in range(len(gas)):
            leftover_gas+=gas[i]-cost[i]
            if leftover_gas<0:
                leftover_gas=0
                start=(i+1) #from here next check starts
        return start
        
