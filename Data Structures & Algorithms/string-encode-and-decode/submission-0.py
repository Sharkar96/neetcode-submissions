class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""

        for stringa in strs:
            result += str(len(stringa))+"#"+stringa
        
        return result

    def decode(self, s: str) -> List[str]:
        result = list()

        i = 0
        while i < len(s):
            
            j = i + 1
            while s[j] != "#":
                j = j + 1
            number = int(s[i : j])
            i = j + 1

            result.append(s[i : i + number])

            i = i + number




        return result
        

            

            


                


