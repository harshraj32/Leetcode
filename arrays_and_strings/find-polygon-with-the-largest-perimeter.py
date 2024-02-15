class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)
        total = sum(nums)
           
        i = n -1
        while(i>0):
            total -= nums[i]
            if total > nums[i]:

                return total + nums[i]
            i -= 1

        

        return -1
        