print('*** Reading E-Book ***')
s = input('Text , Highlight : ').split(',')

for i in range(0,len(s[0]), 1):
    if(s[0][i] == s[1][0]):
        print('[', s[0][i], ']', sep='', end='')
    else:
        print(s[0][i], end='')