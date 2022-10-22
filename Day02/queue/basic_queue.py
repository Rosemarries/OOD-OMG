class Queue:
    def __init__(self, list = None):
        self.list = [] if(list == None) else list
    def __str__(self):
        return self.list
    def enqueue(self, i):
        self.list.append(i)
    def dequeue(self):
        return self.list.pop(0)
    def size(self):
        return len(self.list)
    def isEmpty(self):
        return False if(self.size() > 0) else True
    def index(self, item):
        for i in range(0, self.size()):
            if(item == self.list[i]):
                return i
        return -1


q = Queue()

li = []
inp = input('Enter Input : ').split(',')
for e in inp:
    li.append([i for i in e.split()])
for i in range(0,len(li)):
    if(li[i][0] == 'E'):
        q.enqueue(li[i][1])
        print("Add", li[i][1], "index is", q.index(li[i][1]))
    elif(li[i][0] == 'D'):
        if(not q.isEmpty()):
            print("Pop", q.dequeue(), "size in queue is", q.size())
        else:
            print("-1")

if(not q.isEmpty()):
    print("Number in Queue is : ", q.__str__())
else:
    print("Empty")