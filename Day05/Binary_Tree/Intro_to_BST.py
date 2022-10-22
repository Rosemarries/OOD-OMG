class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            now = self.root
            while now:
                if data < now.data:
                    if not now.left:
                        now.left = Node(data)
                        break
                    now = now.left
                else:
                    if not now.right:
                        now.right = Node(data)
                        break
                    now = now.right
        else:
            self.root = Node(data)
        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)