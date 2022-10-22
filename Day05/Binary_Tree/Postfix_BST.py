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
    
    def is_leaf(self, curnode):
        return True if not curnode.left and not curnode.right else False

    def insert(self, data):
        operators = "+-*/"
        if self.root:
            now = self.root
            while now:
                if now.right:
                    if now.right.data not in operators:
                        if now.left:
                            now = now.left
                        else:
                            now.left = Node(data)
                            break
                    now = now.right
                else:
                    now.right = Node(data)
        else:
            self.root = Node(data)
        return self.root

    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


T = BST()
inp = [i for i in input('Enter Postfix : ').split()]
for i in inp[::-1]:
    root = T.insert(i)
T.printTree(root)