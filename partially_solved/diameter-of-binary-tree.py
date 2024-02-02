# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        
        def diameterBinary(root):

            if root == None:
                return 0

            else:

                right = diameterBinary(root.right)
                left = diameterBinary(root.left)
                diameter[0] = max(diameter[0],right+left)
                return max(right+1 ,left+1)

            
        diameterBinary(root)
        return diameter[0]

            