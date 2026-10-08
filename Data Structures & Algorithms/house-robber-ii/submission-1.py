class Solution:
    def rob(self, nums: List[int]) -> int:
    
        def rob1(nums):
            rob1, rob2 = 0, 0

            for i, num in enumerate(nums):
                    
                tmp = max(rob1, num + rob2)
                rob2 = rob1
                rob1 = tmp
            return rob1
        if len(nums) == 1: return nums[0] 
        return max(rob1(nums[:-1]), rob1(nums[1:]))
            

