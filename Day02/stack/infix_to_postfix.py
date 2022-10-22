class Stack :
    def __init__(self,list = None) :
        self.list = [] if(list == None) else list
    def isEmpty(self) :
        return False if(self.size() > 0) else True
    def push(self,data) :
        self.list.append(data)
    def pop(self) :
        return self.list.pop()
    def size(self) :
        return len(self.list)
    def peek(self) :
        return self.list[-1]


def infix2postfix(exp) :
    s = Stack()
    str = ""
    for i in exp:
        if (i in ['+', '-', '*', '/', '(', ')']):
            if(not s.isEmpty()):
                if(i in ['+', '-']):
                    if(s.peek() in ['*', '/', '(']):
                        while(not s.isEmpty() and s.peek()!='('):
                            str += s.pop()
                    elif(s.peek() in ['+', '-']):
                        str += s.pop()

                elif(i==')'):
                    while(s.peek() != '('):
                        str += s.pop()
                    s.pop()
                
                elif(i in ['*', '/']):
                    if(s.peek() in ['*', '/', '(']):
                        str += s.pop()

            if(i != ')'):
                s.push(i)
        else:
            str += i
    while(not s.isEmpty()):
        str += s.pop()
    return str


print(" ***Infix to Postfix***")
token = input("Enter Infix expression : ")

print("PostFix : ")
print(infix2postfix(token))