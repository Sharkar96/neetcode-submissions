class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        #i is the current num we are aveluating
        #currentCombination is the current list that should sum to the target
        #total is the sum of the elements in currentCombination
        def dfs(i, currentCombination, total):
            if total == target:
                res.append(currentCombination.copy())
                return
            if i>= len(nums) or total > target:
                return
            
            # scelgo di usare l'i-esimo elemento
            currentCombination.append(nums[i])
            # i non si aggiorna perché vorrei poterlo riusare un' altra volta
            dfs(i, currentCombination, total + nums[i])
            #rimuovo l'elemento appena inserito per l'altro branch dove decido di non usarlo piu'
            currentCombination.pop()
            dfs(i + 1, currentCombination, total)

        dfs(0, [], 0)
        return res   

        