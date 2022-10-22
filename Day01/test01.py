
print('*** Converting hh.mm.ss to seconds ***')
t = input('Enter hh mm ss : ').split()

err = False
pre = -1
sum = 0
for i in range(0,3,1):
    tt = int(t[i])
    if(i == 0):
        if(tt >= 0):
            sum += tt*60*60
            continue
        else:
            err = True
            pre = i
            break
    else:
        if(tt >= 0 and tt <= 59):
            sum += tt*60**(2-i)
            continue
        else:
            err = True
            pre = i
            break

if(err == True):
    if(pre == 0):
        print('hh(', end='')
    elif(pre == 1):
        print('mm(', end='')
    else:
        print('ss(', end='')
    print(t[pre], ') is invalid!', sep='')
else:
    print(t[0].zfill(2), ':', t[1].zfill(2), ':', t[2].zfill(2), ' = ', sep='', end='')
    if(sum // 1000 > 0):
        print(sum//1000, ',', sep='', end='')
    print(sum%1000 , ' seconds', sep='', end='')