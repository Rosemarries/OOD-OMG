class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        s = ""
        if self.head == None:
            return "List is empty"
        now = self.head
        while now != None:
            s += str(now.data) + ("->" if now.next else "")
            now = now.next
        return f"link list : {s}"
    def isEmpty(self):
        return False if self.head != None else True
    def size(self):
        sized = 0
        now = self.head
        while now != None:
            now = now.next
            sized += 1
        return sized
    def append(self, data):
        newNode = Node(data)
        now = self.head
        if self.head == None:
            self.head = newNode
        else:
            while now.next != None:
                now = now.next
            now.next = newNode
    def insert(self, index, data):
        newNode = Node(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return f"index = {index} and data = {data}"
        elif index > 0 and index < self.size():
            now = self.head
            for _ in range(index-1):
                now = now.next
            newNode.next = now.next
            now.next = newNode
            return f"index = {index} and data = {data}"
        elif index == self.size():
            now = self.head
            while now.next:
                now = now.next
            now.next = newNode
            return f"index = {index} and data = {data}"
        else:
            return "Data cannot be added"

linked = LinkedList()
inp = input("Enter Input : ").split(",")
for i in range(len(inp)):
    if i == 0:
        indexs = inp[0].split()
        for j in range(len(indexs)):
            linked.append(indexs[j])
    else:
        indexs = inp[i].split(":")
        print(linked.insert(int(indexs[0]), indexs[1]))
    print(linked)