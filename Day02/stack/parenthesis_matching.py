class Stack:
    def __init__(self):
        self.items = []
    def push(self,i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return False if(self.size() > 0) else True
    def size(self):
        return len(self.items)

ls = input('Enter expresion : ')
s = Stack()
n1 = 0
n2 = 0
unmatch = False

for e in ls:
    if(e in ['(','{','[']):
        s.push(e)
        n1 += 1
    elif(e in [')','}',']']):
        n2 += 1
        if(s.size() > 0):
            ex = s.pop()
            if((ex != '(' and e == ')') or (ex != '{' and e == '}') or (ex != '[' and e == ']')):
                print(ls, "Unmatch open-close  ")
                unmatch = True
                break
        else:
            unmatch = False
            break

if(s.size() > 0 and unmatch == False):
    print(ls, "open paren excess  ", s.size(), ": ", end="")
    for e in range(0,s.size()):
        print(s.pop(), end="")
elif(n1 != n2 and unmatch == False):
    print(ls, "close paren excess")
elif(unmatch == False):
    print(ls, "MATCH")