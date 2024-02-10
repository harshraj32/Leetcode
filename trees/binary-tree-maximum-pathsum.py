# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self,  root: Optional[TreeNode]) -> int:

        ans = [root.val]
        def pathSum(root):

            if root is None:
                return 0
        
            left = max(0, pathSum(root.left))
            right = max(0, pathSum(root.right))
            ans[0] = max(ans[0], root.val + left + right)
            return root.val + max(left,right)

        pathSum(root)
        return ans[0]
        
