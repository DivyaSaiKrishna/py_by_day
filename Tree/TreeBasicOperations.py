from Binary_Tree import BinaryTree
#inserting element into trees
class TreeBasicOperation:
    def insert(self,root, data):
        if root is None:
            return BinaryTree(data)
        if root.data < data:
            root.right = self.insert(root.right, data)
        else:
            #all greater values on left
            root.left = self.insert(root.left, data)
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=' ')
            self.inorder(root.right)
        


if __name__ == "__main__":
    treeOp = TreeBasicOperation()
    root = None

    for value in [50, 30, 70, 20, 40, 60, 80]:
        root = treeOp.insert(root, value)

    print("Inorder Traversal of Tree:")
    treeOp.inorder(root)




    
        