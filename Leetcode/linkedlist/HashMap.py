class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0
    def __str__(self):
        s = ""
        now = self.head
        while now:
            s += str(now.data) + ("->" if now.next else "")
            now = now.next
        return s
    def put(self, index, value):
        newNode = node(value)
        if index >= 0 and index <= self.size:
            if self.head is None or index == 0:
                if index == 0 and self.head != None:
                    newNode.next = self.head
                self.head = newNode
            elif index > 0 and index < self.size:
                now = self.head
                for i in range(index-1):
                    now = now.next
                newNode.next = now.next
                now.next = newNode
            elif index == self.size:
                now = self.head
                while now.next:
                    now = now.next
                now.next = newNode
            self.size += 1
            return f"Put index {index} : {value}"
        return f"Cannot put index {index} : {value}"
    def get(self, index):
        if index >= 0 and index < self.size and self.head:
            now = self.head
            for i in range(index):
                now = now.next
            return f"Index {index} : {now.data}"
        return f"Cannot find index {index}"
    def remove(self, index):
        if index >= 0 and index < self.size and self.head:
            value = None
            if index == 0:
                value = self.head.data
                self.head = self.head.next
            elif index > 0 and index < self.size:
                now = self.head
                for i in range(index-1):
                    now = now.next
                value = now.next.data
                now.next = None if now.next is None else now.next.next
            self.size -= 1
            return f"Remove index {index} : {value}"
        return f"Cannot remove index {index}"

inp = input("Enter input : ").split(",")
l = linkedlist()
for e in inp:
    e = e.split()
    if e[0] == "P":
        e = e[1].split(":")
        l.put(int(e[0]), int(e[1]))
    elif e[0] == "G":
        print(l.get(int(e[1])))
    elif e[0] == "R":
        print(l.remove(int(e[1])))
    print(l)