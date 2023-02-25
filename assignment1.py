#[Problem 1]
def ntom(n,m,mult_counter=0): #mult_counter calculates the number of multiplications used
    if m==1:       #when m is 1
        print(f"{mult_counter} multiplications were used")
        return n 
    elif m % 2==0: # when m is even
        mult_counter += 1
        return ntom(n**2,m/2,mult_counter)
    else:          # m is odd
        mult_counter += 2
        return n*(ntom(n**2,(m-1)/2,mult_counter))

print("[Problem 1]: ")
print(ntom(2,61))
print("")

#[Problem 2]

#[Part 1]
def SingleCourse(List):
    courses = {}
    for i in List:                                  #O(n)
        if i in courses:
            courses[i] += 1                         #O(1)
        else:
            courses[i] = 1                          #0(1)
    for key,value in courses.items():               #O(n)
        if value == 1:
            print(f"{key} have only {value} hour!") #O(1)

print("[Problem 2(a)]")    
SingleCourse(["B101","CS141","M102","C102","P102","C102","P102","M102","B101"])

#[Part 2]
def findSingle(List):
    Sum = ((len(List)+1)*(len(List)+3))//4 #Sum of 2n integers
    for i in List: 
        Sum -= i
    #After the loop has run, the only part of sum remaining will be that one missing number
    print(Sum)

print("[Problem 2(b)]")
findSingle([1,1,2,2,3,4,4,5,5,6,7,6,7])
print("")

#[Problem 3]

#[Part 1]
def ThisSort1(List,k):
    aux1 = [i for i in range(k-1,len(List),k)]            #Indices of multiples in the list
    aux2 = [i for i in range(len(List)) if i not in aux1] #Indices of non-multiples in the list

    #Sorting in ascending order
    #Considers only elements with index in aux1
    for i in range(len(aux1)):                            
        current = List[aux1[i]]
        j = i - 1
        while j>=0 and current < List[aux1[j]]:
            List[aux1[j+1]] = List[aux1[j]]
            j -= 1
        List[aux1[j+1]] = current

    #Sorting in descending order
    #Considers only elements with index in aux2
    for i in range(len(aux2)):
        current = List[aux2[i]]
        j = i-1
        while j>=0 and current > List[aux2[j]]:
            List[aux2[j+1]] = List[aux2[j]]
            j -= 1
        List[aux2[j+1]] = current
    return List

print("Problem 3(a)")
print(ThisSort1([31,12,21,55,14,1,51,30,2,7],3))


#[Part 2]
def ThisSort(List,k):
    
    #Sorting the elements at nth position in Ascending order
    for i in range(k-1,len(List),k):
        current = List[i]
        j = i-k
        while j>=0 and List[j] > current:
            List[j+k] = List[j]
            j-=k
        List[j+k]=current
    
    #Sorting rest of the elements in Descending order
    for i in range(len(List)):
        if (i+1)%k!=0:          #Discards elements with k-divisible position
            current = List[i]
            if i%k == 0:
                j = i-2
            else:
                j = i-1
            while j>=0 and List[j]<current:
                if (j+2)%k==0:
                    List[j+2]=List[j]
                else:
                    List[j+1]=List[j]
                if j%k == 0:
                    j-=2
                else:
                    j-=1
            if (j+2)%k == 0:
                List[j+2]=current
            else:
                List[j+1]=current
    return List    
    
print("[Problem 3(b)]")
print(ThisSort([31,12,21,55,22,1,51,30,2,7],3))
print("")

#[Problem 4]
def inversion(List):
    count = 0  #Counts the number of inversion pairs
    for i in range(1,len(List)):
        current = List[i]
        j = i-1
        while j>=0 and current<List[j]:  #loop runs when List[i]<List[j]. i>j since j = j-1 => inversion pair
            List[j+1] = List[j]
            count += 1                   #Adds the count whenever loop is run
            j -= 1
        List[j+1] = current
    print(f"The List has {count} inversion pairs!")
print("[Problem 4]: ")
inversion([1,3,2,9,5,6,2,21,11])

