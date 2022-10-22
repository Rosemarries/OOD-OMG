class Node:
    def __init__(self, data, index=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.index = index
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None
    def printTree(self, node, level=0):
        if node:
            self.printTree(node.right, level+1)
            print("     " * level, node.data)
            self.printTree(node.left, level+1)
    def add(self, data):
        if not self.root:
            self.root = Node(data)
            return
        index = 0
        queue = [self.root]
        while queue:
            now = queue.pop(0)
            if now.left:
                index += 1
                queue.append(now.left)
            else:
                now.left = Node(data, index+1)
                break
            if now.right:
                index += 1
                queue.append(now.right)
            else:
                now.right = Node(data, index+1)
                break
    def search(self, index=0):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            now = queue.pop(0)
            if now.index == index:
                return now
            if now.left:
                queue.append(now.left)
            if now.right:
                queue.append(now.right)
    def sum(self, node):
        if not self.root:
            return 0
        sum_T = 0
        queue = [node]
        while queue:
            now = queue.pop(0)
            sum_T += now.data
            if now.left:
                queue.append(now.left)
            if now.right:
                queue.append(now.right)
        return sum_T
        

T = Tree()
inp = input("Enter Input : ").split("/")
l1 = list(map(int, inp[0].split()))
l2_1 = list(inp[1].split(","))
l2 = []
for e in l2_1:
    l2.append(list(map(int, e.split())))

for e in l1:
    T.add(e)
    # T.printTree(T.root)
    # print("-"*20)
print(T.sum(T.root))

for e in l2:
    sum_1 = T.sum(T.search(e[0]))
    sum_2 = T.sum(T.search(e[1]))
    # print(f"index{e[0]} = {T.search(e[0]).data}")
    # print(f"index{e[1]} = {T.search(e[1]).data}")
    print(e[0], ">" if sum_1 > sum_2 else ("=" if sum_1 == sum_2 else "<"), e[1], sep="")