class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

class linkedlist:
    def __init__(self, l=[]):
        self.head = None
        if self.head:
            for i in range(len(l)):
                self.append(l[i])
        self.size = len(l)
    def head(self):
        return self.head
    def append(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
        else:
            now = self.head
            while now.next:
                now = now.next
            now.next = newNode
    def add(self, h2):
        l = []
        while h1 and h2:
            l.append(int(h1.data) + int(h2.data))
            h1 = h1.next
            h2 = h2.next
        return l

inp = input("Enter Input : ").split()
l1 = inp[0].split(",")
l2 = inp[1].split(",")
listed_1 = linkedlist(l1)
listed_2 = linkedlist(l2)
print(listed_1.add(listed_2.head()))