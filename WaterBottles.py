class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        max_bottles_drunk = numBottles
        currently_drunk = 0
        remainder = 0
        
        while numBottles >= numExchange:
            currently_drunk, remainder = divmod(numBottles, numExchange)
            max_bottles_drunk += currently_drunk
            numBottles = currently_drunk + remainder
            
        return max_bottles_drunk