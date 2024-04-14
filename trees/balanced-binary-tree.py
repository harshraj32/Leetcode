# current
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):

            if node is None:
                return [True, 0]

            left = dfs(node.left)
            right = dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


# previous
"""class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = ["true"]
        print("first",ans[0])
        def balance(root):

            if root is None:
                return 0

            else:
                left = balance(root.left) 
                right = balance(root.right)

                if left > right:
                    diff = left - right

                else:
                    diff = right - left
                
                if diff > 1:

                    ans[0] = "False"
                    

            return max(right+1, left+1)
        balance(root)
        print(ans)
        if ans[0] == 'False':
            print(1)
            return False
        else: 
            return True"""
