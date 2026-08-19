class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        if len(nums) < 3:
            return ret

        #order array
        ordered = sorted(nums)

        #for every number get the rest and perform two sums with pointers
        for i, num in enumerate(ordered):
            if i>0 and num == ordered[i-1]:
                continue

            l = i + 1 
            r = len(ordered) - 1
            while l<r:
                if ordered[l] + ordered[r]  + num < 0:
                    l+=1
                elif ordered[l] + ordered[r] + num > 0:
                    r-=1
                else:
                    ret.append([num, ordered[l], ordered[r]])

                    l += 1
                    while l<r and ordered[l] == ordered[l - 1]:
                        l+=1
        
        return ret
            


            
        