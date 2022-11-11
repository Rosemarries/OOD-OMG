class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self, data: list = []):
        self.list = data

    def enQueue(self, data):
        self.list.append(data)

    def deQueue(self, data):
        if len(self.list):
            return self.list.pop(0)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root: Node, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insert(root.left, data)
        if data > root.data:
            root.right = self.insert(root.right, data)
        return root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def preOrder(self, root):
        if root:
            print(root.data, end=" ")
            self.preOrder(root.left)
            self.preOrder(root.right)

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data, end=" ")
            self.inOrder(root.right)

    def bfs(self,data)


inp = [int(x) for x in input().split()]
T = BST()
root = None
for i in inp:
    root = T.insert(root, i)
T.printTree(root)
T.preOrder(root)
print()
T.inOrder(root)
