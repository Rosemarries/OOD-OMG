class Node:
    def __init__(self, data, index=0, level=0, left=None, right=None):
        self.data = data
        self.index = index
        self.level = level
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None
        self.max_level = 0
    def printTree(self, node, level=0):
        if node:
            self.printTree(node.right, level+1)
            print("     "*level, node.data)
            self.printTree(node.left, level+1)
    def add(self, data=0, index=0):
        if not self.root:
            self.root = Node(data)
            return
        level = 0
        count = 0
        queue = [self.root]
        while queue:
            now = queue.pop(0)
            if now.left:
                queue.append(now.left)
            else:
                now.left = Node(data, index, level+1)
                break
            if now.right:
                queue.append(now.right)
            else:
                now.right = Node(data, index, level+1)
                break
            count += 1
            if count == pow(2, level):
                count = 0
                level += 1
        self.max_level_tree()
    def max_level_tree(self):
        if self.root:
            self.max_level = 0
            now = self.root
            while now:
                now = now.left
                self.max_level += 1
    def sum(self):
        if not self.root:
            return 0
        sum_all = 0
        queue = [self.root]
        while queue:
            now = queue.pop(0)
            if now.left:
                queue.append(now.left)
            if now.right:
                queue.append(now.right)
            sum_all += now.data
        return sum_all
    def delete(self, level=0):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            minus = 0
            now = queue.pop(0)
            if now.level == level:
                if now.left and now.right:
                    minus = min(now.left.data, now.right.data)
                    now.left.data -= minus
                    now.right.data -= minus
                elif now.left:
                    minus = now.left.data
                    now.left.data -= minus
                else:
                    minus = now.data
                now.data = minus
            if now.left:
                queue.append(now.left)
            if now.right:
                queue.append(now.right)

T = Tree()
inp = input("Enter Input : ").split("/")
total = int(inp[0])
listed = list(map(int, inp[1].split()))
if total//2 + 1 != len(listed):
    print("Incorrect Input")
else:
    for i in range(total//2):
        T.add(0, i)
    for i in range(len(listed)):
        T.add(listed[i], i+total//2)
    for i in range(T.max_level-1):
        T.delete(T.max_level-i-2)
    print(T.sum())