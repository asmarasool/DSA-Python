# it has a node and each node at most has two children: right and left
# Left child of the node must have a value less than its parent’s value
# Right child of the node must have a value greater than its parent’s value
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # def print_node(self):
    #     print(self.data)

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def inOrderTraversal(self, root):  # Left -> data -> Right
        res = []
        if root:
            res = self.inOrderTraversal(root.left)
            res.append(root.data)
            res = res + self.inOrderTraversal(root.right)
        return res

    def preOrderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preOrderTraversal(root.left)
            res = res + self.preOrderTraversal(root.right)
        return res
####################################
    def postOrderTraversal(self, root):
        res = []
        if root:
            res = res + self.postOrderTraversal(root.left)
            res = res + self.postOrderTraversal(root.right)
            res.append(root.data)
        return res
################################
    def binarysearch(self, wanted):
        if wanted < self.data:
            if self.left is None:
                return str(wanted) + " Not found:("
            return self.left.binarysearch(wanted)
        elif wanted > self.data:
            if self.right is None:
                return str(wanted) + " Not found :("
            return self.right.binarysearch(wanted)
        else:
            print(wanted, "is found :)")




    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


myTree = Node(100)
myTree.insert(95)
myTree.insert(140)
myTree.insert(50)
myTree.insert(150)

print(myTree.inOrderTraversal(myTree), "Inorder")
print(myTree.preOrderTraversal(myTree), "PreOrder")
print(myTree.postOrderTraversal(myTree), "PostOrder")
myTree.print_tree()
print(myTree.binarysearch(1))

