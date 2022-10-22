class node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    nexted = node(l[-1], None)
    for i in range(-1, -len(l) - 1, -1):
        newNode = node(l[i], nexted)
        nexted = newNode
        if(i==0 or i==-len(l)):
            H = newNode
    return H

def printList(H):
    now = H
    while now.next:
        print(f"{now} ", end="")
        now = now.next
    print()

def mergeOrderesList(p,q):
    def removeLastNode(head):
        if head == None:
            return None
        if head.next == None:
            head = None
            return None
        last = head
        while(last.next.next):
            last = last.next
        last.next = None
        return head, last.data
    
    def push_back(head, newElement):
        newNode = node(newElement)
        if(head == None):
            head = newNode
            return
        else:
            temp = head
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
    p, last_p = removeLastNode(p)
    q, last_q = removeLastNode(q)
    if last_p >= last_q:
        push_back(p, last_p)
    else:
        push_back(q, last_q)
    head = None
    while(p is not None or q is not None):
        if(p is not None):
            if(q is None or int(p.data) <= int(q.data)):
                newNode = node(p.data)
                if(head == None):
                    head = newNode
                    now = head
                now.next = newNode
                now = now.next
                p = p.next
                
        if(q is not None):
            if(p is None or int(p.data) > int(q.data)):
                newNode = node(q.data)
                if(head == None):
                    head = newNode
                    now = head
                now.next = newNode
                now = now.next
                q = q.next
       
    return head

#################### FIX comand ####################   
inp = input("Enter 2 Lists : ").split()
L1 = list(map(int, inp[0].split(',')))
L2 = list(map(int, inp[1].split(',')))

LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1, LL2)
print('Merge Result : ',end='')
printList(m)