class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        i , j = 0, 1
        k = 0
        for k in range(n):

            if nums[k] > 0:
                ans[i] = nums[k]
                i += 2
            else:
                ans[j] = nums[k]
                j += 2
            
        
        
        return ans
