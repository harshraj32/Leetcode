
class Node:

    def __init__(self, key) -> None:
        
        self.val = key
        self.right = None
        self.left = None



class Solution:



    def BuildTree(self, postorder, inorder) -> Node:

        if not inorder or not preorder:
            return None

        root = Node(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.BuildTree(preorder[1: mid+1], inorder[:mid])
        root.right = self.BuildTree(preorder[mid+1:], inorder[mid+1: ])


        return root


    def printTree(self, root):

        if not root:
            return None
        
        print(root.val)
        self.printTree(root.left)
        self.printTree(root.right)

if __name__ == "__main__":

    sol = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    tree = sol.BuildTree(preorder, inorder)
    sol.printTree(tree)




