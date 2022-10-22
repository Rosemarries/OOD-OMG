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
    def append(self, data):
        newNode = node(data)
        if not self.head:
            self.head = newNode
        else:
            now = self.head
            while now.next:
                now = now.next
            now.next = newNode
    def BtoD(self):
        decimal = 0
        now = self.head
        while now:
            decimal = decimal*2 + int(now.data)
            now = now.next
        return decimal

inp = input("Enter Input : ").split(',')
listed = linkedlist(inp)
print(listed.BtoD())