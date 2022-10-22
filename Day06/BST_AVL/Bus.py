class Node:
    def __init__(self, data, day=0, left=None, right=None):
        self.data = data
        self.day = day
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None
    def add(self, data):
        if not self.root:
            self.root = Node(data)
            return
        queue = [self.root]
        while queue:
            now = queue.pop(0)
            if now.left:
                queue.append(now.left)
            else:
                now.left = Node(data)
                break
            if now.right:
                queue.append(now.right)
            else:
                now.right = Node(data)
                break
    def find_min(self):
        if not self.root:
            return
        min_day = self.root
        queue = [self.root]
        while queue:
            now = queue.pop(0)
            if min_day.day > now.day:
                min_day = now
            if now.left:
                queue.append(now.left)
            if now.right:
                queue.append(now.right)
        return min_day
    def booking(self, days):
        if not self.root:
            return 0
        min_day = self.find_min()
        min_day.day += days
        return min_day.data

T = Tree()
inp = input("Enter Input : ").split("/")
buses = int(inp[0])
book_bus = list(map(int, inp[1].split()))
for i in range(buses):
    T.add(i+1)
for i in range(len(book_bus)):
    print(f"Customer {i+1} Booking Van {T.booking(book_bus[i])} | {book_bus[i]} day(s)")