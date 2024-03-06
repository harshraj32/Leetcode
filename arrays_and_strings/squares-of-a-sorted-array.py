class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        i = 0
        j = len(nums) - 1
        result = []
        while i <= j:

            if abs(nums[i]) < abs(nums[j]):

                result.append(nums[j] ** 2)
                j -= 1

            else:
                result.append(nums[i] ** 2)
                i += 1

        return result[::-1]
