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

def dec2bin(decnum):
    s = Stack()
    str1 = ""
    while(decnum > 0):
        s.push(decnum % 2)
        decnum //= 2
    while(not s.isEmpty()):
        str1 += str(s.pop())
    return str1
    

print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")

print("Binary number : ",end='')
print(dec2bin(int(token)))