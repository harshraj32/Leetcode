class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        n = len(nums)
        nums1 = sorted(nums)
        ans = []
        i = 0
        while(i < n - 2):
            
            
            if  nums1[i+2] - nums1[i] <= k:
                ans.append([nums1[i], nums1[i+1], nums1[i+2]]) 
            else:
                return []
            i += 3
        return ans

                