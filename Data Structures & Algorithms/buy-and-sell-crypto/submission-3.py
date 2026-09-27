class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        min_left = [0] * n
        min_left[1] = prices[0]
        for i in range(2, n):
            min_left[i] = min(min_left[i - 1], prices[i - 1])

        profit = 0
        for j in range(1, n):
            profit = max(profit, prices[j] - min_left[j])
        
        return profit