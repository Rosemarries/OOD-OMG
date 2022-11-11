class Data:
    def __init__(self, key):
        self.key = key
    def __str__(self):
        return str(self.key)

class Hash:
    def __init__(self, size=0, collision=0, threshold=0):
        self.collision = collision
        self.size = size
        self.table = [None] * size
        self.threshold = threshold/100
    def __str__(self):
        s = ""
        for i in range(self.size):
            s += f"#{i+1}\t{self.table[i]}\n"
        s += "----------------------------------------"
        return s
    def add(self, key):
        print(f"Add : {key}")
        while 1:
            index = key % self.size
            collision_count = 0
            if not self.check_threshold():
                while self.table[index] and collision_count < self.collision:
                    collision_count += 1
                    print(f"collision number {collision_count} at {index}")
                    index = (key % self.size + pow(collision_count, 2)) % self.size
                if collision_count < self.collision:
                    self.table[index] = Data(key)
                    print(self)
                    break
                else:
                    print("****** Max collision - Rehash !!! ******")
                    self.rehash()
            else:
                print("****** Data over threshold - Rehash !!! ******")
                self.rehash()
    def rehash(self):
        prime = self.find_prime()
        for _ in range(prime - self.size):
            self.table.append(None)
        self.size = prime
    def check_threshold(self):
        count = 0
        for i in range(self.size):
            if self.table[i]:
                count += 1
        return True if count >= round(self.size*self.threshold) else False
    def find_prime(self):
        prime = self.size * 2
        while 1:
            is_prime = True
            for j in range(2, prime):
                if prime % j == 0:
                    prime += 1
                    is_prime = False
                    break
            if is_prime:
                return prime


inp = input(" ***** Rehashing *****\nEnter Input : ").split("/")
tableSize, collisionTime, threshold = map(int, inp[0].split())
list_hash = list(map(int, inp[1].split()))

hash = Hash(tableSize, collisionTime, threshold)
for i in range(len(list_hash)):
    if i==0:
        print("Initial Table :")
        print(hash)
    hash.add(list_hash[i])