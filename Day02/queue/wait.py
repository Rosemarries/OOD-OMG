class Queue:
    def __init__(self, list = None):
        self.list = [] if(list == None) else list
    def __str__(self):
        return self.list
    def enqueue(self, i):
        self.list.append(i)
    def dequeue(self):
        if(not self.isEmpty()):
            self.list.pop(0)
    def size(self):
        return len(self.list)
    def isEmpty(self):
        return False if(self.size() > 0) else True
    def index(self, item):
        for i in range(0, self.size()):
            if(item == self.list[i]):
                return i
        return -1


q1 = Queue()
q2 = Queue()
i=0
j=0
t2=0
li = list(input("Enter people : "))
while(len(li) > 0):
    if(not q2.isEmpty()):
        t2 += 1
    if(i%3 == 0):
        q1.dequeue()
    if(t2%2 == 0):
        q2.dequeue()

    if(q1.size() < 5):
        q1.enqueue(li[0])
        li.pop(0)
    elif(q1.size() == 5 and q2.size() < 5):
        q2.enqueue(li[0])
        li.pop(0)

    print(i+1, li, q1.__str__(), q2.__str__())
    i += 1