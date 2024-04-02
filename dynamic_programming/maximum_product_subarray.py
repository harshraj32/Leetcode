class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix , suffix = 1,1
        max_prod = -math.inf
        for i in range(len(nums)):
            suffix *= nums[i]
            prefix *= nums[~i]
            max_prod = max(max_prod, suffix, prefix)
            prefix = prefix or 1
            suffix = suffix or 1

        return max_prod
            
            
        