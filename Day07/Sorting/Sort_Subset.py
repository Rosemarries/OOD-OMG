def sorting(l, n):
    lists = find_list(l, n)
    for i in range(len(lists)-1):
        for j in range(i+1, len(lists)):
            if len(lists[i]) > len(lists[j]):
                lists[i], lists[j] = lists[j], lists[i]
            elif len(lists[i]) == len(lists[j]) and i!=j:
                for k in range(len(lists[i])):
                    if lists[i][k] > lists[j][k]:
                        lists[i], lists[j] = lists[j], lists[i]
                        break
    return "\n".join(map(str, lists)) if len(lists) else "No Subset"

def find_list(l, n):
    lists = []
    for i in range(pow(2, len(l))):
        sums = 0
        temp = []
        used = decimal_to_binary(l, i)
        for j in range(len(used)):
            if used[j] == 1:
                sums += l[j]
                temp.append(l[j])
        if sums == n:
            lists.append(temp)
    return lists

def decimal_to_binary(l, num):
    return list(map(int, format(num, f"#0{len(l)+2}b")[2:]))

def sort_list(l):
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

inp = input("Enter Input : ").split("/")
n = int(inp[0])
l = list(map(int, inp[1].split()))
l = sort_list(l)
print(sorting(l, n))