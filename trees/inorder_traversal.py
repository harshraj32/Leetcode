


class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def Inorder(root):

    if root:

        Inorder(root.left)
        print(root.val, end= " ")
        Inorder(root.right)

def Preorder(root):

    if root:

        print(root.val, end=" ")
        Preorder(root.left)
        Preorder(root.right)

def Postorder(root):

    if root:

        Postorder(root.left)
        Postorder(root.right)
        print(root.val, end=" ")

if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    print("Inorder traversal : ")
    Inorder(root)

    print("\nPreorder traversal : ")
    Preorder(root)

    print("\nPostorder traversal : ")
    Postorder(root)


