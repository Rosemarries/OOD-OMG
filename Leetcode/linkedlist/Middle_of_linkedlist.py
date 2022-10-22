class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self, l=[]):
        self.head = None
        if l != []:
            for i in range(len(l)):
                self.append(l[i])
        self.size = len(l)
    def __str__(self):
        s = ""
        now = self.head
        while now:
            s += str(now.data) + ("->" if now.next else "")
            now = now.next
        return s
    def append(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
        else:
            now = self.head
            while now.next:
                now = now.next
            now.next = newNode
    def middle(self):
        now = self.head
        for i in range(self.size//2):
            now = now.next
        return now
    def from_middle(self):
        middling = self.middle()
        print(f"Middle : {middling.data}")
        while middling:
            print(middling.data, end="," if middling.next else "")
            middling = middling.next

inp = input("Enter Input : ").split(",")
listed = linkedlist(inp)
listed.from_middle()