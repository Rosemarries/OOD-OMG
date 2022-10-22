class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0
    def __str__(self):
        if(self.isEmpty()):
            return "List is empty"
        str = ""
        printval = self.head
        while printval != None:
            str += (printval.data + ("->" if(printval.next != None) else ""))
            printval = printval.next
        return f"link list : {str}"
    def isEmpty(self):
        return True if(self.head == None) else False
    def append(self, data):
        newNode = Node(data)
        self.size += 1
        if(self.isEmpty()):
            self.head = newNode
        else:
            theLast = self.head
            while theLast.next is not None:
                theLast = theLast.next
            theLast.next = newNode
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
                newNode.next = now.next
                now.next = newNode
        else:
            return "Data cannot be added"
        return f"index = {int(index)} and data = {data}"

listed = LinkedList()

inp = input("Enter Input : ").split(",")
l1 = []
for i in range(len(inp)):
    l1.append(inp[i].split(" " if(i==0) else ":"))
for i in range(len(l1)):
    if(i==0):
        if(l1[i] != ['']):
            for j in range(len(l1[i])):
                listed.append(l1[i][j])
    else:
        print(listed.insert(l1[i][0], l1[i][1]))
    print(listed.__str__())