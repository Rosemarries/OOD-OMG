class node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

class linkedlist:
    def __init__(self, head = None):
        self.head = head
        self.size = 0
        self.loop = False
    def __str__(self):
        s = ""
        now = self.head
        while now and not self.loop:
            s += str(now.data) + ("->" if now.next else "")
            now = now.next
        return s if self.size > 0 else "Empty"
    def append(self, data):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
        else:
            now = self.head
            while now.next and not self.loop:
                now = now.next
            now.next = newNode
        self.size += 1
    def set_next(self, index1, index2):
        if not self.head:
            return "Error! {list is empty}"
        if index1 not in range(0, self.size):
            return "Error! {index not in range} : " + f"{index1}"
        if index2 not in range(0, self.size):
            self.append(index2)
            return f"index not in range, append : {index2}"
        else:
            now1 = self.head
            for _ in range(index1):
                now1 = now1.next
            now2 = self.head
            for _ in range(index2):
                now2 = now2.next
            now1.next = now2
            if index1 > index2:
                self.loop = True
            return f"Set node.next complete!, index:value = {index1}:{now1} -> {index2}:{now2}"
    def check_loop(self):
        return "Found loop" if self.loop else "No loop"

listed = linkedlist()
inp = input("Enter input : ").split(",")
for i in range(len(inp)):
    in2 = inp[i].split()
    if in2[0] == "A":
        listed.append(int(in2[1]))
    elif in2[0] == "S":
        nexted = in2[1].split(":")
        print(listed.set_next(int(nexted[0]), int(nexted[1])))
    print(listed)

print(listed.check_loop())
print(listed)