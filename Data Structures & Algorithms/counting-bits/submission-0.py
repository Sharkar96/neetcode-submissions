class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n + 1):
            j = i
            res = 0
            while j > 0:
                res += 1 if j & 1 else 0
                j >>= 1
            output.append(res)

        return output

        