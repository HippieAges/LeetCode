class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = float("-inf")
        min_stock = float("inf")
        
        for price in prices:
            if price < min_stock:
                min_stock = price
            if (new_profit := price - min_stock) > profit:
                profit = new_profit
        return profit