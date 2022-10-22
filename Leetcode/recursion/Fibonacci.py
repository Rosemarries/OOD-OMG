# def fibo(n=0, before=0, now=1, i=0):
#     if n==i+1 or n==2 or n==0:
#         return now if n!=0 else before
#     return fibo(n, now, before+now, i+1)

# inp = int(input("Enter N : "))
# print(fibo(inp))

def fibo(n=0):
    if n == 0 or n == 1:
        return 1 if n > 0 else 0
    return fibo(n-1) + fibo(n-2)

inp = int(input("Enter n : "))
print(f"fibo({inp}) = {fibo(inp)}")