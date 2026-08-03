class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n + 1):
            j = i
            res = 0
            while j > 0:
                j = j & (j - 1)
                res += 1
            output.append(res)

        return output

        