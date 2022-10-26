def insertion(l):
    if not len(l[1]):
        print("sorted")
        return l[0]
    num = l[1].pop(0)
    i = index(l[0], num)
    l[0].insert(i, num)
    print(f"insert {num} at index {i} : {l[0]}", l[1] if len(l[1]) else "")
    return insertion(l)

def index(l, num, i=0):
    if i == len(l) or l[i] >= num:
        return i
    return index(l, num, i+1)

inp = list(map(int, input("Enter Input : ").split()))
print(insertion([[inp[0]], inp[1:]]))