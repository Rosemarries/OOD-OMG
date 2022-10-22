class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class MyHashSet(object):
    def __init__(self, l=[]):
        self.head = None
        for i in range(len(l)):
            self.add(l[i])
    
    def __str__(self):
        s = ""
        now = self.head
        while now:
            s += str(now.data) + ("->" if now.next else "")
            now = now.next
        return s

    def add(self, key):
        newNode = node(key)
        if not self.head:
            self.head = newNode
        else:
            now = self.head
            while now.next:
                now = now.next
            now.next = newNode
        
    def remove(self, key):
        if self.head:
            if self.head.data == key:
                self.head = self.head.next
                return f"Remove {key}"
            else:
                now = self.head
                while now.next:
                    if now.next.data == key:
                        now.next = None if not now.next.next else now.next.next
                        return f"Remove {key}"
                    now = now.next
        return f"Cannot Remove {key}"
        
    def contains(self, key):
        now = self.head
        while now:
            if now.data == key:
                return f"Have {key}"
            now = now.next
        return f"Don't have {key}"


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
inp = input("Enter Input : ").split(',')
for e in inp:
    e = e.split()
    command, value = e
    if command == "A":
        obj.add(value)
    elif command == "C":
        print(obj.contains(value))
    elif command == "R":
        print(obj.remove(value))
    print(obj)