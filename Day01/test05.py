print('*** Fun with countdown ***')
l = [int(x) for x in input('Enter List : ').split()]
l2 = list(reversed(l))
li = []
sum = 0

for i in range(0, len(l2), 1):
    if(l2[i] == 1):
        li2 = []
        j = i
        sum += 1
        while(j+1<len(l2) and l2[j] == l2[j+1] - 1):
            li2.append(l2[j])
            j += 1
        li2.append(l2[j])
        li.append(list(reversed(li2)))

print([sum, list(reversed(li))])
