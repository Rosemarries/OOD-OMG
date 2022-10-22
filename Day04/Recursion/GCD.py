result = 1
def gcd(m, n):
    global result
    if(m % n == 0):
        print(abs(result))
        return
    result = m % n
    gcd(n, result)

n, m = [int(e) for e in input("Enter Input : ").split()]
if(abs(n) > abs(m)):
    min = m
    max = n
else:
    min = n
    max = m
if(n >= 0 and m < 0):
    min = m
    max = n
elif(n < 0 and m >= 0):
    min = n
    max = m
result = min
if(min == 0 and max == 0):
    print("Error! must be not all zero.")
elif(min == 0):
    print(f"The gcd of {max} and {min} is : {abs(max)}")
else:
    print(f"The gcd of {max} and {min} is : ", end="")
    gcd(abs(max),abs(min))