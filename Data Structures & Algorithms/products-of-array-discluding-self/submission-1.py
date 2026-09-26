class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        totmul = 1 
        numOfZeros = 0
        for num in nums:
            if num != 0:
                totmul *= num
            else:
                numOfZeros += 1

        if numOfZeros > 1:
            return [0] * len(nums)

        if numOfZeros == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    output[i] = totmul
                else:
                    output[i] = 0
            return output
        
        for i in range(len(nums)):
            output[i] = totmul // nums[i]


        
        return output

        