class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for el in strs:
            sortedEl = "".join(sorted(el))
            result[sortedEl].append(el)
        
        return list(result.values())
        