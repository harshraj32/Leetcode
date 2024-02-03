class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        diameter = [0]

        def diabinary(root):

            if root is None:
                return 0

            else:
                left = diabinary(root.left)
                right = diabinary(root.right)
                diameter[0] = max(diameter[0], left+right)
        
            return max(left+1, right+1)

        diabinary(root)
        return diameter[0]
