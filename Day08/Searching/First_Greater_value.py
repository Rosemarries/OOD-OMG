inp = input("Enter Input : ").split("/")
list1, list2 = sorted(list(map(int, inp[0].split()))), list(map(int, inp[1].split()))
for e in list2:
    try:
        res = next(x for x, val in enumerate(list1) if val > e)
        print(list1[res])
    except:
        print("No First Greater Value")