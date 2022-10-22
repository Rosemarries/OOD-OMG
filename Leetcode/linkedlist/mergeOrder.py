class node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

def createList(l=[]):
    head = None
    for i in range(len(l)):
        newNode = node(l[i])
        if i == 0:
            head = newNode
        elif head.data > newNode.data:
            newNode.next = head
            head = newNode
        else:
            now = head
            while now.next and now.data <= newNode.data:
                now = now.next
            if now != head and now.next:
                newNode.next = now.next
            now.next = newNode
    return head

def printList(H):
    now = H
    s = ""
    while now:
        s += str(now.data) + " "
        now = now.next
    print(s)

def mergeOrderesList(p,q):
    head = None
    while p or q:
        if (p and not q) or ((p.data <= q.data) if p and q else False):
            newNode = node(p.data)
            p = p.next
        elif (not p and q) or ((p.data > q.data) if p and q else False):
            newNode = node(q.data)
            q = q.next

        if head is None:
            head = newNode
        elif head.data > newNode.data:
            newNode.next = head
            head = newNode
        else:
            now = head
            while now.next and now.data <= newNode.data:
                now = now.next
            if now != head and now.next:
                newNode.next = now.next
            now.next = newNode
    return head

#################### FIX comand #################### 
inp = input("Enter 2 Lists : ").split()
L1 = [int(x) for x in inp[0].split(",")]
L2 = [int(x) for x in inp[1].split(",")]
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)