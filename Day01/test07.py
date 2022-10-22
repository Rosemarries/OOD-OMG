def weirdSubtract(n,k):
    if(k == 0):
        return n
    if(n%10 == 0):
        n //= 10
    else:
        n -= 1
    k -= 1
    return weirdSubtract(n,k)


n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))