def bon(w):
    ch = ''
    for i in range(0, len(w)-1, 1):
        for j in range(i+1, len(w), 1):
            if(w[i] == w[j]):
                ch = w[i]
                break
    return (ord(ch) - ord('a') + 1) * 4


secretCode = input("Enter secret code : ")
print(bon(secretCode))