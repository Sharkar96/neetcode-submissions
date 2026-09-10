class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxArea = 0
        savedI, savedJ = 0, 0
        while i < j:
            newMaxArea = (j - i) * min(heights[i], heights[j])

            if newMaxArea > maxArea:
                savedI, savedJ = i, j
                maxArea = newMaxArea
                
            if heights[i] > heights[j]:
                j = j - 1
            else:
                i = i + 1
        
            

        return maxArea

        



        