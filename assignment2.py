#Problem 1
def compute(List):
    if len(List)<=5:
        if List[2]=="+":
            return int(List[1])+int(List[3])
        else:
            return int(List[1])-int(List[3])
    else:
        for i in range(len(List)):
            if List[i]=="(" and List[i+4]==")":
                merge = compute(List[i:i+5])
                del List[i:i+4]
                List[i] = merge
                break
        return compute(List)

print("Problem 1")
print(compute(list("((3+2)-((1-2)+5))")))
print("")

#Problem 2
def twoProduct(List,Target):
    hashmap = {}
    for i in List:       #O(n)
        if i in hashmap: #Searching in a Dictionary has time complexity O(1)
            print(f"{hashmap[i]} and {i}")
        else:
            hashmap[Target/i]=i #O(1)
print("Problem 2")
twoProduct([1, 5, 6, 8, 13, 17, 22, 45],132)
print("")

#Problem 3
def insertionSort(String,Order):
    hashmap = {Order[i]:i for i in range(0,len(Order))}
    List = [*String]
    for i in range(1,len(String)):
        current = List[i]
        j = i-1
        while j>=0 and hashmap[current]<hashmap[List[j]]:
            List[j+1] = List[j]
            j -= 1
        List[j+1] = current
    return "".join(List)

print("Problem 3")
print(insertionSort("dcabesfshdsakcdc","bacdefshk"))



