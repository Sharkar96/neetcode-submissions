class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        maxCount = 0
        l = 0
        for r, num in enumerate(s):    
            if num in ss:
                while s[l] != num:
                    ss.remove(s[l])
                    l+=1
                ss.remove(s[l])
                l+=1

            ss.add(num)
            maxCount= max(maxCount, r - l + 1)
        
        return maxCount





            


        