class Stack:
    def __init__(self):
        self.items = []
    def push(self,value):
        self.items.append(value)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return False if(self.size() > 0) else True
    def size(self):
        return len(self.items)


inp = input('Enter Input : ').split()
S = Stack()

combo = 0
for e in inp:
    if(S.size() < 2):
        S.push(e)
    else:
        pre1 = S.pop()
        pre2 = S.pop()
        if(e != pre1 or e != pre2):
            S.push(pre2)
            S.push(pre1)
            S.push(e)
        else:
            combo += 1

print(S.size())
if(S.size() == 0):
    print("Empty")
else:
    for e in range(0,S.size()):
        print(S.pop(), end="")
    print()

if(combo > 1):
    print("Combo :", combo, "! ! !")