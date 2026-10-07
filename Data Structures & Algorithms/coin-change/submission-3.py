class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        # try the BFS approach
        q = deque([0])
        layer = 0

        visited = set()
        
        while q:
            layer += 1
            currentLen = len(q)
            for _ in range(currentLen):
                current = q.popleft()
                if current not in visited:
                    visited.add(current)
                    for coin in coins:
                        if current + coin < amount:
                            q.append(current + coin)
                        elif current + coin == amount:
                            return layer
                
        return -1

            

