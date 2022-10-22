def pow_2(n, now=1):
    if now > n:
        return False
    if now == n:
        return True
    return pow_2(n, now*2)

inp = int(input("Enter n : "))
print(pow_2(inp))