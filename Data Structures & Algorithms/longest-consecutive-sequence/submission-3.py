class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset=set(nums)
        longestSeq=0

        i=0
        while(i<len(nums)):
            if (nums[i] - 1) not in numsset:
                length = 1
                currentSeq=nums[i]
                while(currentSeq + length in numsset):
                    length += 1
                longestSeq = max(longestSeq, length)
            i += 1
        return longestSeq
                    
        