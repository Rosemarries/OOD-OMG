class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.used = False
    def __str__(self):
        return str(self.value)

def createLL(LL):
    head = None
    for i in LL:
        newNode = Node(i)
        if(head == None):
            head = newNode
        else:
            now = head
            while now.next:
                now = now.next
            now.next = newNode
    return head

def printLL(head):
    s = ""
    now = head
    while now:
        s += str(now.value) + " "
        now = now.next
    return s

def SIZE(head):
    size = 0
    now = head
    while now:
        size += 1
        now = now.next
    return size

def scarmble(head, b, r, size):
    bottomUp = int(size * b / 100)
    riffle = int(size * r / 100)

    #BOTTOMUP
    now = head
    for i in range(bottomUp - 1):
        now = now.next
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = head
    head = now.next
    now.next = None
    print(f"BottomUp {b:.3f} % : {printLL(head)}")

    #RIFFLE
    now1 = head
    headRiffle = None
    riffling = None
    while now1.used == False:
        now2 = now1.next
        for i in range(riffle-1):
            if(now2 is None):
                break
            now2 = now2.next
        if(now2 != None):
            if(now1.used == False and now2.used == False):
                if(headRiffle == None):
                    headRiffle = Node(now1.value)
                    headRiffle.next = Node(now2.value)
                    now1.used = True
                    now2.used = True
                else:
                    riffling = headRiffle
                    while riffling.next:
                        riffling = riffling.next
                    riffling.next = Node(now1.value)
                    riffling.next.next = Node(now2.value)
                    now1.used = True
                    now2.used = True
        now1 = now1.next
    now1 = head
    while now1:
        if(now1.used == False):
            riffling = headRiffle
            while riffling.next:
                riffling = riffling.next
            riffling.next = Node(now1.value)
            now1.used = True
        now1 = now1.next
    print(f"Riffle {r:.3f} % : {printLL(headRiffle)}")

    #DERIFFLE
    now = head
    while now:
        now.used = False
        now = now.next
    print(f"Deriffle {r:.3f} % : {printLL(head)}")

    #DEBOTTOMUP
    debottomup = size - bottomUp
    now = head
    for i in range(debottomup - 1):
        now = now.next
    tail = head
    while tail.next:
        tail = tail.next
    tail.next = head
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