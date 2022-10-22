class Stack:
    def __init__(self, list = None):
        self.list = [] if(list == None) else list
    def push(self, i):
        self.list.append(i)
    def pop(self):
        if(not self.isEmpty()):
            return self.list.pop()
    def peek(self, i):
        if(i >= -self.size() and i < self.size()):
            return self.list[i]
        return '-1'
    def size(self):
        return len(self.list)
    def isEmpty(self):
        return False if(self.size() > 0) else True

def ManageStack(commands, num = None):
    if(commands == 'A'):
        s.push(int(num))
        print("Add =", num)

    if(not s.isEmpty()):
        if(commands == 'P'):
            print("Pop =", s.pop())

        temp = []
        for j in range(-1,-s.size()-1,-1):
            if(j >= -s.size() and j < s.size()):
                if(commands == 'D'):
                    if(int(s.peek(j)) == int(num)):
                        n = s.peek(j)
                        temp.append(n)
                        print("Delete =", n)
                elif(commands == 'LD'):
                    if(int(s.peek(j)) < int(num)):
                        n = s.peek(j)
                        temp.append(n)
                        print("Delete =", n, "Because", n, "is less than", num)
                elif(commands == 'MD'):
                    if(int(s.peek(j)) > int(num)):
                        n = s.peek(j)
                        temp.append(n)
                        print("Delete =", n, "Because", n, "is more than", num)
        s.list = [x for x in s.list if x not in temp]
    else:
        print('-1')

s = Stack()
ls = []
inp = input("Enter Input : ").split(',')
for e in inp:
    ls.append(e.split())

for i in range(0,len(ls)):
    if(len(ls[i]) == 1):
        ManageStack(ls[i][0])
    else:
        ManageStack(ls[i][0], ls[i][1])

print("Value in Stack =", s.list)