class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self, l=[]):
        self.head = None
        if l != []:
            for i in range(len(l)):
                self.append(int(l[i]))
    def __str__(self):
        s = ""
        now = self.head
        while now:
            s += str(now.data) + ("->" if now.next else "")
            now = now.next
        return s
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
    def merge2list(self, h2):
        merge = None
        now = self.head
        h2 = h2.head
        while now or h2:
            if not now or now.data <= h2.data:
                merge = node(now.data)
                now = now.next
            elif not h2 or now.data <= h2.data:
                merge = node(h2.data)
                h2 = h2.next
            print(merge.data, end=" ")
            merge = merge.next

inp = input("Enter Input : ").split()
l1 = linkedlist([e for e in inp[0].split(",")])
l2 = linkedlist([e for e in inp[1].split(",")])
print(l1.merge2list(l2))