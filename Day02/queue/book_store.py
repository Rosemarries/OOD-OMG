class Queue:
    def __init__(self, list = None):
        self.list = [] if(list == None) else list
    def enqueue(self, i):
        self.list.append(i)
    def dequeue(self):
        if(not self.isEmpty()):
            self.list.pop(0)
    def size(self):
        return len(self.list)
    def isEmpty(self):
        return False if(self.size() > 0) else True
    def listing(self):
        return self.list

l1 = []
l2 = []
i = 0

inp = input("Enter Input : ").split('/')
for e in inp:
    if(i == 0):
        l1.append(e.split())
    else:
        l1.append(e.split(','))
    i += 1

for e in l1[1]:
    l2.append(e.split())

q = Queue(l1[0])
for i in range(len(l2)):
    if(l2[i][0] == 'E'):
        q.enqueue(l2[i][1])
    elif(l2[i][0] == 'D'):
        q.dequeue()

li = []
dupli = False
for i in q.listing():
    if(i not in li):
        li.append(i)
    else:
        dupli = True
        break

if(not dupli):
    print("NO ", end="")
print("Duplicate")