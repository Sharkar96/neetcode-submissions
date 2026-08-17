class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicto = {}
        ret = list()
        for el in nums:
            if el in dicto:
                dicto[el] += 1
            else:
                dicto[el] = 1


        finalList = [[] for _ in range(len(nums) + 1)]

        for num, freq in dicto.items():
            finalList[freq].append(num) 

        count = 0
        for i in range(len(nums), 0, -1):
            while len(finalList[i]) != 0 and count < k:
                topKel = finalList[i].pop(0) 
                ret.append(topKel)
                count += 1

        return ret