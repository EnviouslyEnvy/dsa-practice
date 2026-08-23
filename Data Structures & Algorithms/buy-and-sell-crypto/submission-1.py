class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=float('inf')
        max_profit=0
        for current_price in prices:
            if current_price<lowest:
                lowest=current_price
            max_profit=max(max_profit,current_price-lowest)
        return max_profit