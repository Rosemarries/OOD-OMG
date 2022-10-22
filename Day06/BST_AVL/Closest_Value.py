class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self, key=None):
        self.root = None
        self.closest = None
        self.key = key
    def printTree(self, node, level=0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)
    def add(self, data):
        if not self.root:
            self.root = Node(data)
            self.closest = data
        else:
            if abs(self.closest-self.key) > abs(data - self.key):
                self.closest = data
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

inp = input("Enter Input : ").split("/")
listed = list(map(int, inp[0].split()))
key = int(inp[1])
T = Tree(key)
for e in listed:
    T.add(e)
    T.printTree(T.root)
    print("--------------------------------------------------")
print(f"Closest value of {key} : {T.closest}")