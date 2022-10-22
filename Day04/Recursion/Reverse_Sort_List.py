def reverse(l, n, time):
    if(time == len(l)-1):
        print(f"List after Sorted : {l}")
    else:
        if(n+1 < len(l)):
            if(l[n] < l[n+1]):
                temp = l[n]
                l[n] = l[n+1]
                l[n+1] = temp
            reverse(l, n+1, time)
        else:
            reverse(l, 0, time+1)

n = list(int(e) for e in input("Enter your List : ").split(","))
reverse(n, 0, 0)