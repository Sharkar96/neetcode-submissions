class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = []
        offset = 1
        for i in range(n + 1):
            if i == 0:
                dp.append(0)
            else:
                if i == offset * 2:
                    offset = i*2

                dp.append(1 + dp[i - offset])
                
        return dp