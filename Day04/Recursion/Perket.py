def decimalToBinary(num, max):
    return str(format(num, f"0{max}b"))

def product_sum(listed, sets, product, sum, j):
    max = len(sets)
    if(j == max):
        return abs(product - sum)
    if(sets[j] == "1"):
        product *= listed[j][0]
        sum += listed[j][1]
        # print(f"\t{product} || {sum}")
    return product_sum(listed, sets, product, sum, j+1)

def perket(listed, i, mined):
    max = 2**len(listed)
    if(i == max):
        return mined
    sets = decimalToBinary(i, len(listed))
    # print(f"\tsets = {sets} && len = {max}")
    mins = product_sum(listed, sets, 1, 0, 0)
    if(mined != None):
        if(mins > mined):
            mins = mined
    return perket(listed, i+1, mins)


inp = input("Enter Input : ").split(",")
li = []
for e in inp:
    li.append([int(i) for i in e.split()])

print(perket(li, 1, None))