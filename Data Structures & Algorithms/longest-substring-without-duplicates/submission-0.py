class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charInSub = set()
        first = 0
        maxer = 0

        for second, char in enumerate(s):
            # Shrink window until the duplicate is gone
            while char in charInSub:
                charInSub.remove(s[first])
                first += 1
            
            # Add current char and update max
            charInSub.add(char)
            maxer = max(maxer, second - first + 1)
            
        return maxer

        