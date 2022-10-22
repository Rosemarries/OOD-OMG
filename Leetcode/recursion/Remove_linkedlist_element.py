class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class linkedlist:
    def __init__(self):
        self.head = None
    def print_str(self, now, s=""):
        if now:
            s += str(now.data) + ("->" if now.next else "")
            return self.print_str(now.next, s)
        return s
    def append(self, data, now):
        newNode = node(data)
        if self.head is None:
            self.head = newNode
        else:
            if now.next:
                return self.append(data, now.next)
            now.next = newNode
    def remove(self, data, now):
        if self.head:
            if self.head.data == data:
                self.head = self.head.next
            else:
                if now.next:
                    if now.next.data == data:
                        now.next = None if now.next.next else now.next.next
                    return self.remove(data, now.next)

inp = input("Enter Input : ").split()
print()