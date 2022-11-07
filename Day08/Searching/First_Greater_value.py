def find_first(l, r, listed, key, mode=False):
    mid = (l+r)//2
    if (mode and listed[mid] < key) or (not mode and listed[mid] > key) or (key == listed[mid] and mid+1 < len(listed)):
        return listed[mid] if not mode and key!=listed[mid] else listed[mid+1]
    if not mode and l==0 and listed[mid] > key:
        mode = True
    if l < r:
        return find_first(l+1 if listed[mid]<key else l, r-1 if listed[mid]>key else r, listed, key, mode)
    return "No First Greater Value"

inp = input("Enter Input : ").split("/")
list1, list2 = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for e in list2:
    print(find_first(0, len(list1)-1, sorted(list1), e))