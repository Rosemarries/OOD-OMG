class node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def atTail(self, now):
        if now.next:
            return self.atTail(now.next)
        return now
    def append(self, l=[], i=0):
        newNode = node(l[i])
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            now = self.atTail(self.head)
            newNode.previous = now
            now.next = newNode
            self.tail = newNode
    def print_str(self, now, s=""):
        if now:
            s += str(now.data) + ("->" if now.next else "")
            return self.print_str(now.next, s)
        return s
    def rev_str(self, now, s=""):
        if now:
            s += str(now.data) + ("->" if now.previous else "")
            return self.rev_str(now.previous, s)
        return s

inp = input("Enter Input : ").split()
listed = linkedlist()
for i in inp:
    listed.append(i)
print(listed.print_str(listed.head))
print(listed.rev_str(listed.tail))