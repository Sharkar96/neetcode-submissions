class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSet = set(nums)
        n = len(nums) + 1
        for num in range(n):
            if num not in numsSet:
                return num
           
        