def bubble(l, i=0, sorts=True):
    if sorts and i == len(l)-1:
        return l
    if i == len(l)-1:
        sorts = True
        i = 0
    if l[i] > l[i+1]:
        sorts = False
        l[i], l[i+1] = l[i+1], l[i]
    return bubble(l, i+1, sorts)

inp = list(map(int, input("Enter Input : ").split()))
print(bubble(inp))