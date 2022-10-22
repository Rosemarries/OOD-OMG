class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.used = False
    def __str__(self):
        return str(self.value)

def createLL(LL, i=0, head=None):
    if(i == len(LL)):
        return head
    newNode = Node(LL[i])
    if(head == None):
        head = newNode
    else:
        assignNodeLast(head, newNode)
    return createLL(LL, i+1, head)

def printLL(now, i=0, s=""):
    if(now == None):
        return s
    s += str(now.value) + " "
    return printLL(now.next, i+1, s)

def SIZE(now, size=0, i=0):
    if(now == None):
        return size
    size += 1
    return SIZE(now.next, size, i+1)

def assignLast(now, value):
    if(now.next == None):
        now.next = Node(value)
        return
    return assignLast(now.next, value)

def assignNodeLast(now, node):
    if(now.next == None):
        now.next = node
        return
    return assignNodeLast(now.next, node)

def assign_False(now):
    if(now == None):
        return
    now.used = False
    return assign_False(now.next)

def scarmble(head, b, r, size):
    bottomUp = int(size * b / 100)
    riffle = int(size * r / 100)
    case = 0

    #BOTTOMUP
    now = head
    for i in range(bottomUp - 1):
        now = now.next
    assignNodeLast(head, head)
    head = now.next
    now.next = None
    print(f"BottomUp {b:.3f} % : {printLL(head)}")

    #RIFFLE
    now1 = head
    headRiffle = None
    riffling = None
    riffle_time = 0
    while now1.used == False:
        now2 = now1.next
        for i in range(riffle-1):
            if(now2 is None):
                case = 1
                break
            now2 = now2.next
        if(now2 != None):
            if(now1.used == False and now2.used == False):
                if(headRiffle == None):
                    headRiffle = Node(now1.value)
                    headRiffle.next = Node(now2.value)
                else:
                    riffling = headRiffle
                    while riffling.next:
                        riffling = riffling.next
                    riffling.next = Node(now1.value)
                    riffling.next.next = Node(now2.value)
                riffle_time += 1
                now1.used = True
                now2.used = True
        now1 = now1.next
    now1 = head
    while now1:
        if(now1.used == False):
            assignLast(headRiffle, now1.value)
            now1.used = True
        now1 = now1.next
    assign_False(head)
    print(f"Riffle {r:.3f} % : {printLL(headRiffle)}")

    #DERIFFLE
    headDeriffle = None
    headDeriffle2 = None
    headDeriffle3 = None
    if(r >= 90):
        headDeriffle = head
    else:
        now1 = headRiffle
        for i in range(riffle_time - 1):
            now1 = now1.next.next
            if(headDeriffle == None):
                headDeriffle = Node(headRiffle.value)
                headDeriffle.next = Node(now1.value)
                headRiffle.used = True
            else:
                assignLast(headDeriffle, now1.value)
            now1.used = True
        now1 = now1.next.next
        if(headDeriffle == None):
            headDeriffle = headRiffle
        else:
            now1 = headRiffle.next
            for i in range(riffle_time - 1):
                now1 = now1.next.next
                now1.used = True
                if(headDeriffle2 == None):
                    headDeriffle2 = Node(headRiffle.next.value)
                    headDeriffle2.next = Node(now1.value)
                    headRiffle.next.used = True
                else:
                    assignLast(headDeriffle2, now1.value)

            now1 = headRiffle
            while now1:
                if(now1.used == False):
                    if(headDeriffle3 == None):
                        headDeriffle3 = Node(now1.value)
                        if(now1.next != None):
                            headDeriffle3.next = Node(now1.next.value)
                            now1 = now1.next
                        else:
                            break
                    else:
                        assignLast(headDeriffle3, now1.value)
                    now1.used = True
                now1 = now1.next
            # print(printLL(headDeriffle2))
            # print(printLL(headDeriffle3))
            if(case == 1):
                assignNodeLast(headDeriffle, headDeriffle3)
                assignNodeLast(headDeriffle, headDeriffle2)
            else:
                assignNodeLast(headDeriffle, headDeriffle2)
                assignNodeLast(headDeriffle, headDeriffle3)
    print(f"Deriffle {r:.3f} % : {printLL(headDeriffle)}")

    #DEBOTTOMUP
    debottomup = size - bottomUp
    now = head
    assignNodeLast(head, head)
    for i in range(debottomup - 1):
        now = now.next
    head = now.next
    now.next = None
    print(f"Debottomup {b:.3f} % : {printLL(head)}")

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)