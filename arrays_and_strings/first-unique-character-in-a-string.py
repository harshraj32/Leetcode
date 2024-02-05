class Solution:
    def firstUniqChar(self, s: str) -> int:

        dict1 = {}

        #dict1 - {l : (count, index)}

        for i, x in enumerate(s):
            if x in dict1:
                count, index = dict1[x]
                dict1[x] = [count + 1, i]
            else:
                dict1[x] = [1, i]

        
        for x in dict1.values():
            if x[0] == 1:
                return x[1]

        return -1

        