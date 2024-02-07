class Solution:
    def frequencySort(self, s: str) -> str:
        dict1 = Counter(s)
        return ''.join([x*dict1[x] for x in sorted(dict1, key = lambda x: dict1[x], reverse = True)])




        