# current
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            diameter = max(diameter, left + right)
            return max(1 + left, 1 + right)

        dfs(root)
        return diameter


# previous
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = [0]

        def diabinary(root):

            if root is None:
                return 0

            else:
                left = diabinary(root.left)
                right = diabinary(root.right)
                diameter[0] = max(diameter[0], left + right)

            return max(left + 1, right + 1)

        diabinary(root)
        return diameter[0]
