class Solution:
    def findMin(self, nums: List[int]) -> int:
        #the ideas is take the middle, confront the two segment first middle and middle last, take the one that is decreasing, continue
        left = 0
        right = len(nums) - 1
        middle = len(nums) // 2
        res = nums[middle]


        while nums[left] > nums[right]:
            if nums[left] <= nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

            middle = (right + left) // 2
            res = min(res, nums[middle])

        
        res = min(res, nums[left])

        return res
                

                