from re import S


print('*** Fun With Drawing ***')
n = int(input('Enter input : '))

arr = [['x']*(4*n-3)]*(4*n-3)
for i in range(0,n):
    for j in range(i,4*n-3-2*i,1):
        for k in range(i,4*n-3-2*i,1):
            if i%2 == 0:
                arr[j][k] = '#'
            else:
                arr[j][k] = '.'

for i in range(0,4*n-3):
    for j in range(0,4*n-3):
        print(arr[i][j], end="")
    print()