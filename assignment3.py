#[Problem 1]
def find_pop(expression):
    count  = 0
    flag = True
    for i in range(len(expression)):
        if expression[i] == "(":
            count += 1
        elif expression[i] == ")":
            count -= 1
        if count == 1 and not flag:
            return i+1
            break
        flag = False

def evaluate(expression):
    if len(expression) == 1:
        return int(expression[0])
    elif len(expression) == 5:
        if expression[2] == "+":
            return int(expression[1])+int(expression[3])
        else:
            return int(expression[1])-int(expression[3])
    else:
        a = find_pop(expression)
        if expression[a] == "+":
            return int(evaluate(expression[1:a])) + int(evaluate(expression[a+1:-1]))
        else:
            return int(evaluate(expression[1:a])) - int(evaluate(expression[a+1:-1]))
            
print("Problem 1")
print(evaluate([*"((1+(((5+4)-1)+(2+5)))-(3+3))"]))
print("")

#Problem 2
List = [8, 4, 2, 1]
count = 0
def merge_sort(List):
    if len(List) == 1:
        return List
    mid = len(List) // 2
    left = merge_sort(List[:mid])
    right = merge_sort(List[mid:])
    return merge(left, right)
def merge(left, right):
    global count
    merged_list = list()
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            merged_list.append(left.pop(0))
        else:
            count += len(left)
            merged_list.append(right.pop(0))
    while len(left) != 0:
        merged_list.append(left.pop(0))
    while len(right) != 0:
        merged_list.append(right.pop(0))
    return merged_list

print("Problem 2")
merge_sort(List)
print(count)
print("")

#Problem 3
#Insertion sort, but using binary sort for comparing, rather than looping through every element
def Search(Arr,target,left,right):
    if left == right:
        if Arr[left]<target:
            return left+1
        else:
            return left
    check = (left+right)//2
    if Arr[check]>=target:
        return Search(Arr,target,left,check)
    else:
        if check == left:
            check = right
        return Search(Arr, target, check, right)
def insertionSort(List):
    for i in range(1, len(List)):
        current = List[i]
        j = i - 1
        List.pop(i)
        index = Search(List[: j + 1], current, 0, len(List[: j + 1]) - 1)
        List.insert(index, current)
    return List
a = [4,66,23,12,67,49,22,11]

print("Problem 3")
insertionSort(a)
print(a)
print("")

#Problem 4
def find_median(arr1, arr2):
    #Base condition
    if len(arr1) == 2:
        return (max(arr1[0], arr2[0]), min(arr1[1], arr2[1]))
    right =  len(arr1) // 2 + len(arr1) % 2 - 1
    left = len(arr1) // 2
    if arr1[left] == arr2[right]:
        return (arr1[left], arr1[left])
    elif arr1[left] < arr2[right]:
        return find_median(arr1[left:], arr2[: right + 1])
    else:
        return find_median(arr1[: left + 1], arr2[right:])
        
list1 = [3,5,6,7,9]
list2 = [5,8,9,11,23]
print("Problem 4")
print(find_median(list1,list2))