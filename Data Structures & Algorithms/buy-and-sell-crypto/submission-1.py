class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cost_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] - cost_price > profit:
                profit= prices[i] - cost_price
            if cost_price>prices[i]:
                cost_price=prices[i]
        return profit