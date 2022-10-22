class Queue:
    def __init__(self, list = None):
        self.list = [] if(list == None) else list
    def enqueue(self, i):
        self.list.append(i)
    def dequeue(self):
        return self.list.pop(0)
    def size(self):
        return len(self.list)
    def isEmpty(self):
        return False if(self.size() > 0) else True
    def listing(self):
        return self.list

activity = ['Eat', 'Game', 'Learn', 'Movie']
location = ['Res.', 'ClassR.', 'SuperM.', 'Home']

inp = input("Enter Input : ").split(',')
l1 = []
l2 = []
for e in inp:
    l1.append(e.split())
# print(l1)
for e in l1:
    for i in range(len(e)):
        l2.append(e[i].split(':'))
# print(l2)

q1 = Queue()
q2 = Queue()
for i in range(len(l2)):
    if(i%2 == 0):
        q1.enqueue(l2[i])
    else:
        q2.enqueue(l2[i])

print("My   Queue = ", end="")
for i in range(len(l1)):
    print(l1[i][0], end="")
    if(i != len(l1) - 1):
        print(", ", end="")
print()

print("Your Queue = ", end="")
for i in range(len(l1)):
    print(l1[i][1], end="")
    if(i != len(l1) - 1):
        print(", ", end="")
print()

print("My   Activity:Location = ", end="")
for i in range(len(l2)):
    if(i % 2 == 0):
        print(activity[int(l2[i][0])], ":", location[int(l2[i][1])], sep="", end="")
        if(i != len(l2) - 2):
            print(", ", end="")
print()

print("Your Activity:Location = ", end="")
for i in range(len(l2)):
    if(i % 2 == 1):
        print(activity[int(l2[i][0])], ":", location[int(l2[i][1])], sep="", end="")
        if(i != len(l2) - 1):
            print(", ", end="")
print()

# print(q1.listing())
score = 0
for i in range(q1.size()):
    l1 = q1.dequeue()
    l2 = q2.dequeue()
    if(l1 == l2):
        score += 4
    elif(l1[0] == l2[0]):
        score += 1
    elif(l1[1] == l2[1]):
        score += 2
    else:
        score += -5

if(score >= 7):
    print("Yes! You're my love! : ", end="")
elif(score >= 0):
    print("Umm.. It's complicated relationship! : ", end="")
else:
    print("No! We're just friends. : ", end="")
print("Score is ", score, ".", sep="")