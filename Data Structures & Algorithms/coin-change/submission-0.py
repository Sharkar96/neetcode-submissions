class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        memo = {}

        def dfs(rem):
            #ritorneremo sempre il numero di monete per arrivare a rem
            if rem == 0: return 0 #caso base
            if rem in memo: return memo[rem] #memoization

            minCoins = amount + 1
            for coin in coins:
                # calcolo il nuovo remaining
                newRem = rem - coin
                if newRem >= 0: 
                    minCoins = min(minCoins, 1 + dfs(newRem))
  
            memo[rem] = minCoins # mi salvo il minor numero di monete per amount
            return memo[rem]

        ret = dfs(amount)

        return -1 if ret > amount else ret


        