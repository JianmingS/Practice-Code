class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ret = numBottles

        while numBottles >= numExchange:
            numBottles = numBottles - numExchange + 1
            ret += 1
        
        return ret
