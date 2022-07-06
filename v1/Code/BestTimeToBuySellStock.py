class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buying_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > buying_price:
                current_profit = prices[i] - buying_price
                if current_profit > max_profit:
                    max_profit = current_profit
            else:
                buying_price = prices[i]
        return max_profit