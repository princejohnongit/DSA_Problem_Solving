class Solution:
    def canJump(self, nums: List[int]) -> bool:
        battery_charge=0
        n=len(nums)
        for seen_battery in nums:
            if battery_charge<0: ''' 
                      in such case the car go on due to inerita
                      so gas can be zero as, gas have an opportunity to get updated at the next index
                      EVEN THOUGH GAS IS ZERO next one iteration can possibly fill the car
                      if didn't then the gas is negative
                      ''''
                return False
            elif battery_charge<seen_battery:
                battery_charge=seen_battery
            battery_charge-=1
        return True
