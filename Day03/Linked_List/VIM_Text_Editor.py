class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = Node("|")
        self.tail = self.head
        self.size = 0
    def __str__(self):
        s = ""
        now = self.head
        while now:
            s += now.data + " "
            now = now.next
        return s
    def insert(self, data):
        newNode = Node(data)
        now = self.head
        if(now.data == "|"):
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
        else:
            while(now.next.data != "|"):
                now = now.next
            newNode.previous = now
            newNode.next = now.next
            now.next.previous = newNode
            now.next = newNode
        self.size += 1
    def left(self):
        now = self.head
        while now.data != "|":
            now = now.next
        if now != self.head:
            prev = now.previous
            dataInPrev = prev.data
            prev.data = now.data
            now.data = dataInPrev
    def right(self):
        now = self.head
        while now.data != "|":
            now = now.next
        if now != self.tail:
            nexted = now.next
            dataInNext = nexted.data
            nexted.data = now.data
            now.data = dataInNext
    def backspace(self):
        if(self.head.data != "|"):
            now = self.head
            if(now.data != "|"):
                while now.next.data != "|":
                    now = now.next
                if(now == self.head):
                    now.next.previous = None
                    self.head = now.next
                    now = None
                else:
                    now.previous.next = now.next
                    now.next.previous = now.previous
                    now = None
    def delete(self):
        if(self.tail.data != "|"):
            now = self.head
            while now.data != "|":
                now = now.next
            now = now.next
            if(now != self.tail):
                now.previous.next = now.next
                now.next.previous = now.previous
                now = None
            else:
                self.tail = now.previous
                now.previous.next = None
                now = None

listed = LinkedList()
l = []
inp = input("Enter Input : ").split(",")
for e in inp:
    l.append(e.split())
for i in range(len(l)):
    if(l[i][0] == "I"):
        listed.insert(l[i][1])
    elif(l[i][0] == "L"):
        listed.left()
    elif(l[i][0] == "R"):
        listed.right()
    elif(l[i][0] == "B"):
        listed.backspace()
    elif(l[i][0] == "D"):
        listed.delete()
print(listed)