# current
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):

            if node is None:
                return None

            left = dfs(node.left)
            right = dfs(node.right)

            node.left = right
            node.right = left
            return node

        dfs(root)

        return root


# previous
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None:
            return

        else:
            # right = root.right
            # left = root.left

            root.left = self.invertTree(root.right)
            root.right = self.invertTree(root.left)

        return root
