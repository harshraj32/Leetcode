class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict1 = {}
        max1 = -math.inf
        for i in nums:
            if i not in dict1:
                dict1[i] = 1

            else:
                dict1[i] += 1
            max1 = max(max1, dict1[i])
        sorted(dict1, reverse=True)
        print(dict1, max1)
        sum1 = 0
        for i, v in dict1.items():
            if v == max1:
                sum1 += v
        return sum1
