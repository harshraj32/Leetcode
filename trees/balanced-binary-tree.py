class Solution:
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
            return True