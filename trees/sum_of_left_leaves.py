# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        totalsum = 0
        def dfs(root):
            nonlocal totalsum
            if root == None:
                return 0
            if root.left and not root.left.left and not root.left.right:
                totalsum += root.left.val

            left = dfs(root.left)
            right = dfs(root.right)
            
            return root.val
        
        dfs(root)
        return totalsum
        



        