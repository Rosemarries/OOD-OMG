def checkThreeCombo(n):
    arr = []
    for i in range(0, len(n)-2, 1):
        for j in range(i+1, len(n)-1, 1):
            for k in range(j+1, len(n), 1):
                if(n[i] + n[j] + n[k] == 5):
                    arr.append(sorted([n[i], n[j], n[k]]))
    return unique(arr)

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

num = [int(x) for x in input('Enter Your List : ').split()]

if(len(num) < 3):
    print('Array Input Length Must More Than 2')
else:
    print(checkThreeCombo(num))