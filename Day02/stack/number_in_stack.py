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

s = Stack()
temp = []
ls = []
inp = input("Enter Input : ").split(',')
for e in inp:
    ls.append(e.split())

for i in range(0,len(ls)):
    if(ls[i][0] == 'A'):
        s.push(int(ls[i][1]))
        print("Add =", ls[i][1])
        
    if(not s.isEmpty()):
        if(ls[i][0] == 'P'):
            print("Pop =", s.pop())

        temp = []
        for j in range(-1,-s.size()-1,-1):
            if(j >= -s.size() and j < s.size()):
                if(ls[i][0] == 'D'):
                    if(int(s.peek(j)) == int(ls[i][1])):
                        n = s.peek(j)
                        temp.append(n)
                        print("Delete =", n)
                elif(ls[i][0] == 'LD'):
                    if(int(s.peek(j)) < int(ls[i][1])):
                        n = s.peek(j)
                        temp.append(n)
                        print("Delete =", n, "Because", n, "is less than", ls[i][1])
                elif(ls[i][0] == 'MD'):
                    if(int(s.peek(j)) > int(ls[i][1])):
                        n = s.peek(j)
                        temp.append(n)
                        print("Delete =", n, "Because", n, "is more than", ls[i][1])
        s.list = [x for x in s.list if x not in temp]
    else:
        print('-1')

print("Value in Stack =", s.list)