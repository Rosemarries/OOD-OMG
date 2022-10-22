def find_max(l=[]):
    if len(l) == 1:
        return l[0]
    max = find_max(l[1:])
    return max if max > l[0] else l[0]

inp = input("Enter input : ").split()
l = [int(e) for e in inp]
print(f"Max = {find_max(l)}")