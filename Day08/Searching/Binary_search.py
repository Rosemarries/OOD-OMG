def bi_search(l, r, arr, x):
    mid = (l + r)//2
    if arr[mid] == x:
        return True
    if l < r:
        return bi_search(l+1 if arr[mid]<x else l, r-1 if arr[mid]>x else r, arr, x)
    return False

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))