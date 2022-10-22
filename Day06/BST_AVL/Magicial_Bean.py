class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.root = None
    def add(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            now = self.root
            while now:
                if data < now.data:
                    print("L", end="")
                    if not now.left:
                        now.left = Node(data)
                        break
                    now = now.left
                elif data > now.data:
                    print("R", end="")
                    if not now.right:
                        now.right = Node(data)
                        break
                    now = now.right
        print("*")

T = Tree()
inp = list(map(int, input("Enter Input : ").split()))
for e in inp:
    T.add(e)