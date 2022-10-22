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

    def printTree(self, node, key=None, level=0):
        if node != None:
            self.printTree(node.right, key, level + 1)
            print('     ' * level, node.data*3 if key and node.data > key else node.data)
            self.printTree(node.left, key, level + 1)


T = BST()
inputing = input("Enter Input : ").split("/")
inp = [int(i) for i in inputing[0].split()]
key = int(inputing[1])
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("-"*50)
T.printTree(root, key)