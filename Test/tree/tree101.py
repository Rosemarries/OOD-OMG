class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return self.data

class Tree:
    def __init__(self):
        self.root = None
    def printTree(self, now=None):
        if not now:
            return
        self.printTree(now.left)
        # s += str(now.data) + ("->" if now.left or now.right else "")
        print(now.data, end=" ")
        self.printTree(now.right)
    def minValue(self, node):
        now = node
        while now.left:
            now = now.left
        return now
    def insert(self, data):
        data = int(data)
        newNode = Node(data)
        if not self.root:
            self.root = newNode
        else:
            now = self.root
            while now:
                if data < now.data:
                    if not now.left:
                        now.left = newNode
                        break
                    else:
                        now = now.left
                else:
                    if not now.right:
                        now.right = newNode
                        break
                    else:
                        now = now.right
    def remove(self, now, data):
        if not now:
            return now
        if now.data < data:
            now.left = self.remove(now.left, data)
        elif now.data > data:
            now.right = self.remove(now.right, data)
        else:
            if not now.left and not now.right:
                return None
            if not now.left:
                temp = now.right
                now = None
                return temp
            elif not now.right:
                temp = now.left
                now = None
                return temp
            # successorParent = now
            # successor = now.right
            # while successor.left:
            #     successorParent = successor
            #     successor = successor.left
            # if successorParent != now:
            #     successorParent.left = successor.right
            # else:
            #     successorParent.right = successor.right
            # now.data = successor.data
            temp = self.minValue(now.right)
            now.data = temp.data
            now.right = self.remove(now.right, temp.data)
        return now

tree = Tree()
inp = list(int(e) for e in input("Enter Input : ").split())
for e in inp:
    tree.insert(e)
tree.remove(tree.root, inp[0])
tree.printTree(tree.root)