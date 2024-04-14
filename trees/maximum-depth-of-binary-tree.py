# current
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        def dfs(node):
            nonlocal depth
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            depth = max(depth, 1 + left, 1 + right)

            return max(1 + left, 1 + right)

        dfs(root)
        return depth


# previous
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    distance = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        distance = 0

        def binaryDepth(root):
            if root == None:
                return 0

            else:
                right = binaryDepth(root.right)
                left = binaryDepth(root.left)

                self.distance = 1 + max(left, right)
            return self.distance

        ans = binaryDepth(root)
        return ans
