def box(l, num):
    boxes = [0] * num
    index = 0
    average_case = sum(l)//num
    for i in range(len(l)):
        if (boxes[index] > average_case or boxes[index]+l[i] > round(average_case+2*average_case/5)) and boxes[index]!=0:
            index += 1 if index != num-1 else 0
        if boxes[index] <= average_case:
            boxes[index] += l[i]
    return max(boxes)

inp = input("Enter Input : ").split("/")
list1 = list(map(int, inp[0].split()))
boxs = int(inp[1])
print(f"Minimum weigth for {boxs} box(es) = {box(list1, boxs)}")