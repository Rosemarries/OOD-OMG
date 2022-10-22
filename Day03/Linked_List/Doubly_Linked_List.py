class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def __str__(self):
        str = ""
        printval = self.head
        while printval != None:
            str += (printval.data + ("->" if(printval.next != None) else ""))
            printval = printval.next
        return f"linked list : {str}"
    def str_reverse(self):
        str = ""
        printval = self.head
        while printval != None:
            str = (("->" if(printval.next != None) else "") + printval.data) + str
            printval = printval.next
        return f"reverse : {str}"
    def isEmpty(self):
        return True if(self.head == None) else False
    def append(self, data):
        newNode = Node(data)
        self.size += 1
        if(self.isEmpty()):
            self.head = newNode
            self.tail = newNode
        else:
            theLast = self.head
            while theLast.next is not None:
                theLast = theLast.next
            newNode.previous = theLast
            theLast.next = newNode
            self.tail = newNode
    def insert(self, index, data):
        newNode = Node(data)
        if(int(index) >= 0 and int(index) <= self.size):
            self.size += 1
            if(int(index) == 0):
                newNode.next = self.head
                self.head = newNode
            elif(int(index) == self.size):
                self.append(data)
            else:
                now = self.head
                for i in range(int(index)-1):
                    if(now.next == None):
                        break
                    now = now.next
                newNode.previous = now
                newNode.next = now.next
                now.next = newNode
        else:
            return "Data cannot be added"
        return f"index = {int(index)} and data = {data}"
    def remove(self, data):
        index = 0
        now = self.head
        if(now != None):
            if(int(now.data) == int(data)):
                self.head = now.next
                now = None
                return f"removed : {int(data)} from index : 0"
        while(now != None):
            if(int(now.data) == int(data)):
                if(now.next == None):
                    self.tail = now.previous
                break
            index += 1
            prev = now
            now = now.next
        if(now == None):
            return "Not Found!"
        prev.previous = now.previous.previous
        prev.next = now.next
        now = None
        return f"removed : {int(data)} from index : {int(index)}"


listed = LinkedList()
inp = input("Enter Input : ").split(',')
l1 = []
l2 = []
for e in inp:
    l1.append([i for i in e.split()])
for e in l1:
    l2.append([e[0], [i for i in e[1].split(":")]])

for e in l2:
    if(e[0] == "A"):
        listed.append(e[1][0])
    elif(e[0] == "Ab"):
        listed.insert(0, e[1][0])
    elif(e[0] == "I"):
        print(listed.insert(e[1][0], e[1][1]))
    elif(e[0] == "R"):
        print(listed.remove(e[1][0]))
    print(listed.__str__())
    print(listed.str_reverse())