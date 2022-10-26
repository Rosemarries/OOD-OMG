def sorting(l, i=0, j=1, sorts=True):
    if sorts and i+j == len(l):
        return " ".join(map(str, l))
    if i+j == len(l):
        sorts = True
        i, j = [0, 1]
    if l[i] >= 0 and l[i+j] >= 0:
        if l[i] > l[i+j]:
            sorts = False
            l[i], l[i+j] = l[i+j], l[i]
    return sorting(l, i+1 if(l[i+j]>=0) else i, j+1 if(l[i+j]<0) else 1, sorts)

inp = list(map(int, input("Enter Input : ").split()))
print(sorting(inp))