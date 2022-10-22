def num_grid(lst):
  for i in range(0, len(lst), 1):
    for j in range(0, len(lst[i]), 1):
      if(lst[i][j] == '-'):
        sum = 0
        if(lst[i-1][j-1] == '#' and i>0 and j>0):
          sum += 1
        if(lst[i-1][j] == '#' and i>0):
          sum += 1
        if(i>0 and j+1<len(lst[i])):
          if(lst[i-1][j+1] == '#'):
            sum += 1
        if(lst[i][j-1] == '#' and j>0):
          sum += 1
        if(j+1<len(lst[i])):
          if(lst[i][j+1] == '#'):
            sum += 1
        if(j>0 and i+1<len(lst)):
          if(lst[i+1][j-1] == '#'):
            sum += 1
        if(i+1<len(lst)):
          if(lst[i+1][j] == '#'):
            sum += 1
        if(i+1<len(lst) and j+1<len(lst[i])):
          if(lst[i+1][j+1] == '#'):
            sum += 1
        lst[i][j] = str(sum)

  return lst

print('*** Minesweeper ***')
lst_input = []
input_list = input('Enter input(5x5) : ').split(",")

for e in input_list:
  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")
print("\n",*num_grid(lst_input),sep = "\n")