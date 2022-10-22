class SandQ:
    def __init__(self, list = None):
        self.list = [] if(list == None) else list
    def push(self, i):
        self.list.append(i)
    def pop(self):
        return self.list.pop()
    def dequeue(self):
        return self.list.pop(0) if(not self.isEmpty()) else ''
    def insert(self, i, c):
        self.list.insert(i, c)
    def peek(self):
        return self.list[-1]
    def look(self, i):
        if(i >= -self.size() and i < self.size()):
            return self.list[i]
    def size(self):
        return len(self.list)
    def isEmpty(self):
        return False if(self.size() > 0) else True
    def listing(self):
        return self.list
    def __str__(self, n):
        s = ""
        for i in self.list:
            s += i
        return s if(not self.isEmpty()) else ("Empty" if(n == 0) else "ytpmE")


n = SandQ()
m = SandQ()
bomb = SandQ()
scoreN = 0
scoreM = 0
failed = 0

inp = input("Enter Input (Normal, Mirror) : ").split()

# MIRROR
for i in range(-1,-len(inp[1]) - 1,-1):
    if(m.size() < 2):
        m.push(inp[1][i])
    else:
        pre1 = m.pop()
        pre2 = m.pop()
        if(inp[1][i] != pre1 or inp[1][i] != pre2):
            m.push(pre2)
            m.push(pre1)
            m.push(inp[1][i])
        else:
            bomb.push(pre1)
            scoreM += 1

# NORMAL
for i in range(len(inp[0])):
    x = ''
    if(n.size() < 2):
        n.push(inp[0][i])
    else:
        if(i >= 2):
            pre1 = n.pop()
            pre2 = n.pop()
            if(inp[0][i] != pre1 or inp[0][i] != pre2):
                n.push(pre2)
                n.push(pre1)
                n.push(inp[0][i])
            else:
                if(not bomb.isEmpty()):
                    x = bomb.dequeue()
                    if(x != pre1 or x != pre2):
                        n.push(pre2)
                        if(x != pre1 or x != inp[0][i]):
                            n.push(pre1)
                            n.push(x)
                        else:
                            failed += 1
                            scoreN += 1
                    else:
                        failed += 1
                    n.push(inp[0][i])
                else:
                    scoreN += 1

print("NORMAL :")
print(n.size())
print(n.__str__(1)[::-1])
print(scoreN, "Explosive(s) ! ! ! (NORMAL)")
if(failed != 0):
    print("Failed Interrupted", failed, "Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
print(m.size())
print(m.__str__(0)[::-1])
print("(RORRIM) ! ! ! (s)evisolpxE", scoreM)