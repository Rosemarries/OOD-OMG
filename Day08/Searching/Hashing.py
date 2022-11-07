class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class Hash:
    def __init__(self, size=0, collision=0):
        self.collision = collision
        self.size = size
        self.table = [None] * size
        self.print_full = False
    def __str__(self):
        s = ""
        for i in range(self.size):
            s += f"#{i+1}\t{self.table[i]}\n"
        s += "---------------------------"
        return s
    def ascii(self, key):
        return sum([ord(ele) for ele in key])
    def add(self, key, value):
        index = self.ascii(key) % self.size
        collision_count = 0
        if not self.check_full():
            while self.table[index] and collision_count < self.collision:
                collision_count += 1
                print(f"collision number {collision_count} at {index}")
                index = (self.ascii(key) % self.size + pow(collision_count, 2)) % self.size
            if collision_count < self.collision:
                self.table[index] = Data(key, value)
            else:
                print("Max of collisionChain")
            print(self)
        elif self.check_full() and not self.print_full:
            print("This table is full !!!!!!")
            self.print_full = True
    def check_full(self):
        count = 0
        for i in range(self.size):
            if self.table[i]:
                count += 1
        return True if count == self.size else False


inp = input(" ***** Fun with hashing *****\nEnter Input : ").split("/")
tableSize, collisionTime = map(int, inp[0].split())
list_hash = list(e.split() for e in inp[1].split(","))

hash = Hash(tableSize, collisionTime)
for e in list_hash:
    hash.add(e[0], e[1])