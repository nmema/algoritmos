'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
time complexity -> O(n)
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = prices[0]
        for price in prices:
            if price < min:
                min = price
            if (price - min) > profit:
                profit = price - min
        return profit