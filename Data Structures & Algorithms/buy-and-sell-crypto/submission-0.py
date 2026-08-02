class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        buy = 0
        maxVal = 0
        for i in range(len(prices)):
            if prices[sell] <= prices[buy]:
                buy = sell
                sell += 1
            elif prices[sell] > prices[buy]:
                maxVal = max(maxVal, prices[sell] - prices[buy])
                sell += 1
        
        return maxVal
            
     
        