class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums.sort()
        longest = 0
        currentStreak = 1
        for i, num in enumerate(nums):
            if i == 0: continue

            if num == nums[i - 1] + 1:
                currentStreak += 1
            elif num != nums[i - 1]:
                longest = max(longest, currentStreak)
                currentStreak = 1

        return max(longest, currentStreak)

        