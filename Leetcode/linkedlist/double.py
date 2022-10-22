class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def __str__(self):
        s = ""
        now = self.head
        while now:
            s += str(now.data) + ("->" if now.next else "")
            now = now.next
        return f"linked list : {s}"
    def str_reverse(self):
        s = ""
        now = self.tail
        while now:
            s += str(now.data) + ("->" if now.previous else "")
            now = now.previous
        return f"reverse : {s}"
    def isEmpty(self):
        return False if self.head else True
    def size(self):
        sized = 0
        now = self.head
        while now:
            sized += 1
            now = now.next
        return sized
    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
    def insert(self, index, data):
        newNode = Node(data)
        if index >= 0 and index <= self.size():
            if index == 0:
                if self.head:
                    newNode.next = self.head
                    self.head.previous = newNode
                    self.head = newNode
                else:
                    self.append(data)
            elif index > 0 and index < self.size():
                now = self.head
                for _ in range(index-1):
                    now = now.next
                newNode.next = now.next
                newNode.previous = now
                now.next.previous = newNode
                now.next = newNode
            elif index == self.size():
                self.append(data)
            return f"index = {index} and data = {data}"
        else:
            return "Data cannot be added"
    def remove(self, data):
        if self.head:
            index = 0
            if self.head.data == data:
                if self.size() == 1:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.previous = None
            else:
                now = self.head
                while now.data != data:
                    now = now.next
                if now == self.tail:
                    self.last = self.tail.previous
                else:
                    now.next.previous = now.previous
                    now.previous.next = now.next
            return f"removed : {data} from index : {index}"
        else:
            return "Not found"

listed = linkedlist()
inp = input("Enter Input : ").split(",")
for i in range(len(inp)):
    kuyArn = inp[i].split()
    if kuyArn[0] == "A":
        listed.append(kuyArn[1])
    elif kuyArn[0] == "Ab":
        print(listed.insert(0, kuyArn[1]))
    elif kuyArn[0] == "I":
        kuy = kuyArn[1].split(":")
        print(listed.insert(int(kuy[0]), kuy[1]))
    elif kuyArn[0] == "R":
        print(listed.remove(kuyArn[1]))
    print(listed)
    print(listed.str_reverse())