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
    def preOrder(self, now):
        if not now:
            return
        print(now.data, end=" ")
        self.preOrder(now.left)
        self.preOrder(now.right)
    def inOrder(self, now):
        if not now:
            return
        self.inOrder(now.left)
        print(now.data, end=" ")
        self.inOrder(now.right)
    def postOrder(self, now):
        if not now:
            return
        self.postOrder(now.left)
        self.postOrder(now.right)
        print(now.data, end=" ")
    def breadth(self):
        val = ""
        queue = [self.root]
        values = []
        while len(queue):
            now = queue.pop(0)
            values.append(now.data)
            if now.left:
                queue.append(now.left)
            if now.right:
                queue.append(now.right)
        for e in values:
            val += str(e) + " "
        print(val)


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
# T.printTree(T.root)

print(f"Preorder : ", end="")
T.preOrder(T.root)
print(f"\nInorder : ", end="")
T.inOrder(T.root)
print(f"\nPostorder : ", end="")
T.postOrder(T.root)
print("\nBreadth : ", end="")
T.breadth()