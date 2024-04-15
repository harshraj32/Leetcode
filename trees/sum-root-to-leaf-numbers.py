# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        summ = []

        def dfs(node, path):
            if node is None:
                return

            if not node.left and not node.right:
                summ.append(path + str(node.val))

            dfs(node.left, path + str(node.val))
            dfs(node.right, path + str(node.val))
            return

        dfs(root, "")
        print(summ)
        return sum([int(x) for x in summ])
