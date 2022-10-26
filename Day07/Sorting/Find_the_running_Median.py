def merge(left, right):
    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result

def merge_sort(l):
    if len(l) <= 1:
        return l
    half = len(l)//2
    left = merge_sort(l[:half])
    right = merge_sort(l[half:])
    return merge(left, right)


l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "merge sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    l1 = []
    for e in l:
        l1.append(e)
        merge_list = merge_sort(l1)
        half = len(merge_list)//2
        print(f"list = {l1} : median = {'{:.1f}'.format(merge_list[half] if len(merge_list)%2==1 else (merge_list[half]+merge_list[half-1])/2)}")