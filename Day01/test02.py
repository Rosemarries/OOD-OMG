print('*** multiplication or sum ***')
a = input('Enter num1 num2 : ').split()

print('The result is ', end='')
if(int(a[0]) * int(a[1]) > 1000):
    print(int(a[0]) + int(a[1]))
else:
    print(int(a[0]) * int(a[1]))