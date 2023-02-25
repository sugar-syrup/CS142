#Problem 1
print("Problem 1")

#Part 1
print("Part 1")

def transition(arr,start,stop):
    mid = start+stop//2
    if arr[mid]==arr[mid+1]:
        if arr[mid]==1:
            return transition(arr,mid,stop)
        else:
            return transition(arr,start,mid)
    else:
        return mid+1

List1 = [1,1,1,1,1,2,2,2]
print(transition(List1,0,len(List1)))

#Part 2
print("Part 2")
def F(L1,L2):
    diff = 0
    for i in L1:
        diff += i
    for j in L2:
        diff -= j
    return diff
    
def oddOne(arr,start,stop):
    if len(arr)%2!=0:
        arr += [1]
        stop += 1
    mid = (start+stop)//2
    if arr[mid]==2:
        return mid
    if F(arr[start:mid],arr[mid:stop])>0:
        return oddOne(arr,start,mid)
    else:
        return oddOne(arr,mid,stop)
        
        
List3 = [1,1,1,1,2,1,1,1,1,1,1]
print(oddOne(List3,0,len(List3)))
print("")

#Problem 2
print("Problem 2")
#Part 1
print("Part 1")

def mySort(arr,base):
    if len(arr) <= base:
        for i in range (1,len(arr)):
            current = arr[i]
            j = i-1
            while j>=0 and current<arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = current
        return arr
    else:
        mid = len(arr)//2
        left = mySort(arr[:mid],base)
        right = mySort(arr[mid:],base)
        aux = []
        while len(left)>0 and len(right)>0:
            if left[0]>right[0]:
                aux.append(right[0])
                del right[0]
            else:
                aux.appen(left[0])
                del left[0]
        if len(left) > 0:
            aux += left
        if len(right) > 0:
            aux += right
        return aux
        
List2 = [9,8,7,6,5,4,3,2,1]
print(mySort(List2,3))   


#Part 2(a)
print("Part 2(a)")
def Ways(n):
    if n==2 or n==1:
        return 1
    elif n%2==0:
        return Ways(n-1)+Ways(n/2)
    else:
        return Ways(n-1)
        
print(Ways(16)) 

#Part 2(b)
print("Part 2(b)")
knownWays = {1:1,2:1}
def betterWays(n):
    if n in knownWays:
        return knownWays[n]
    else:
        if n%2==0:
            x = betterWays(n-1)+betterWays(n/2)
            knownWays[n] = x
            return x
        else:
            x = betterWays(n-1)
            knownWays[n] = x
            return x
print(betterWays(16)) 
print("")


#Problem 3
print("Problem 3")

def kthelem(arr1, arr2, l1, l2, k): 
    if l1 == 1 or l2 == 1:
        if l2 == 1:
            arr2, arr1 = arr1, arr2
            l2 = l1
        if k == 1:
            if arr1[0]>arr2[0]:
                return arr2[0]
            else:
                return arr1[0]
        elif k == l2 + 1:
            if arr1[0]<arr2[0]:
                return arr2[0]
            else:
                return arr1[0]
        else:
            if arr2[k-1] < arr1[0]:
                return arr2[k-1]
            else:
                if arr1[0]>arr2[k-2]:
                    return arr1[0]
                else:
                    return arr2[k-2]
 
    mid1 = int((l1-1)/2)
    mid2 = int((l2-1)/2)
    
    if mid1 + mid2 + 1 < k:
        if arr1[mid1] < arr2[mid2]:
            return kthelem(arr1[mid1+1:], arr2, l1-mid1-1, l2, k-mid1-1)
        else:
            return kthelem(arr1, arr2[mid2+1:], l1, l2-mid2-1, k-mid2-1)
    else:
        if arr1[mid1] < arr2[mid2]:
            return kthelem(arr1, arr2[:mid2+1], l1, mid2+1, k)
        else:
            return kthelem(arr1[:mid1+1], arr2, mid1+1, l2, k)


arr1 = [1,6,8,10,11,12,12,13,19]
arr2 = [2,4,7,7,8]

print(kthelem(arr1,arr2,len(arr1),len(arr2),10))