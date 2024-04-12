class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax = [-math.inf] * n
        rightmax = [-math.inf] * n
        max1 = leftmax[0]
        max2 = rightmax[0]
        for i in range(n):
            max1 = max(max1, height[i])
            leftmax[i] = max1
            max2 = max(max2, height[~i])
            rightmax[~i] = max2

        ans = 0
        for i in range(n):
            if min(leftmax[i], rightmax[i]) - height[i] > 0:
                ans += min(leftmax[i], rightmax[i]) - height[i]
        return ans
