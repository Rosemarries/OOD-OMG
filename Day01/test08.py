def mod_position(arr, s):
    st = []
    i = s-1
    while(i < len(arr)):
        st.append(arr[i])
        i += s
    return st



print('*** Mod Position ***')
x = input('Enter Input : ').split(',')
print(mod_position(x[0], int(x[1])))