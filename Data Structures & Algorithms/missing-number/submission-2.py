class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summ=0.5*n*(n+1)
        cumulatSum=0
        for num in nums:
            cumulatSum+=num

        return int(summ-cumulatSum)
        