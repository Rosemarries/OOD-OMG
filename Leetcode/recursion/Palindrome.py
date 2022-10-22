def palindrome(l=[]):
    if len(l) == 1:
        return True
    if l[0] != l[-1]:
        return False
    return palindrome(l[1:-1])

inp = input("Enter input : ")
print(palindrome(inp))