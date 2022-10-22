class node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class linkedlist:
    def __init__(self, l=[]):
        self.head = None
        self.tail = None
        if l != []:
            for i in range(len(l)):
                self.append(l[i])
    def append(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
    def __str__(self):
        s = ""
        now = self.head
        while now:
            s += str(now.data) + ("->" if now.next else "")
            now = now.next
        return s
    def rev_str(self):
        s = ""
        now = self.tail
        while now:
            s += str(now.data) + ("->" if now.previous else "")
            now = now.previous
        return s

inp = input("Enter Input : ").split(",")
listed = linkedlist(inp)
print(listed)
print(listed.rev_str())