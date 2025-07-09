from Binary_Tree import BinaryTree
import sys
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
    
    def findMax(self, root, maxData):
        
        if root is None:
            return 0
        if root.data > maxData:
            maxData = root.data
        leftMax = self.findMax(root.left,maxData)
        rightMax = self.findMax(root.right, maxData)
        return max(maxData , leftMax, rightMax)

    def findElement(self, root, eleData):
        if not root:
            return 0
        if root.data == eleData:
            return 1
        else:
            foundLeft = self.findElement(root.left, eleData)
            foundRight = self.findElement(root.right, eleData)
            if foundLeft == 1:
                return 1
            if foundRight == 1:
                return 1
        return 0

        


if __name__ == "__main__":
    treeOp = TreeBasicOperation()
    root = None

    for value in [50, 30, 70, 20, 40, 60, 80]:
        root = treeOp.insert(root, value)

    print("Max of Tree:")
    print(treeOp.findMax(root, 0))

    print("Inorder Traversal of Tree:")
    treeOp.inorder(root)

    print("find element in Tree:")
    print(treeOp.findElement(root, 76))
    print(treeOp.findElement(root, 70))

    



    
        