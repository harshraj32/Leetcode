class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for s in strs:
            temp = sorted(s)
            temp_s = ''
            for i in temp:           
                temp_s += i

            if temp_s in dict1:
                dict1[temp_s].append(s)
            else:
                dict1[temp_s] = [s]
        
        return list(dict1.values())
