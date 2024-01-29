
class Node:

    def __init__(self, key) -> None:
        
        self.val = key
        self.right = None
        self.left = None



class Solution:



    def BuildTree(self, postorder, inorder) -> Node:

        if not inorder or not postorder:
            return None

        root = Node(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.BuildTree(postorder[: mid], inorder[:mid])
        root.right = self.BuildTree(postorder[mid:-1], inorder[mid+1:  ])


        return root


######

    def printTree(self, root):

        if not root:
            return None
        
        print(root.val)
        self.printTree(root.left)
        self.printTree(root.right)

if __name__ == "__main__":

    sol = Solution()
    postorder = [9,15,7,20,3]
    inorder = [9, 3, 15, 20, 7]
    tree = sol.BuildTree(postorder, inorder)
    sol.printTree(tree)




