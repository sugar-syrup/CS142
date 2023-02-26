#Problem 1
def subset_sum_wrapper(arr,target,l):
  def subset_sum(subsets,curr):
    if curr == len(arr):
      return None
    if sum(subsets) > target:
      return None
    if sum(subsets) == target:
      if len(subsets) == l:
        print(subsets)
    subset_sum(subsets+[arr[curr]],curr+1)  
    subset_sum(subsets,curr+1)              
    
  subset_sum([],0)

print("Problem 1")
print("Part 1")
list1 = [3,34,4,12,5,2]
target = 9
k = 2 
subset_sum_wrapper(list1,target,k)

def subset_sum_wrapper(arr, target, l): 
    arr.sort()
    aux = abs(arr[0])   
    arr = [i+aux for i in arr]
    target = target + l*aux 
    def subset_sum(curr, weight, curr_sub):
        if weight + arr[curr] > target:
            return False  
        elif weight + arr[curr] == target:
            if len(curr_sub) == l-1:
                return True
            else:
                return False
        if curr == len(arr) - 1:
            return False
        else:
          out1 = subset_sum(curr+1, weight + arr[curr], curr_sub + [arr[curr]]) 
          out2 = subset_sum(curr+1, weight, curr_sub)
          return  out1 or out2
    if subset_sum(0, 0, []):
        return "It is possible"
    else:
        return "It is impossible"

print("Part 2")
print(subset_sum_wrapper([3,34,4,5,12,5,2,-3,-5,-4],-12,3))
print()

#Problem 2
#N-queen Problem
n = 5
count = 0

def generate(n):
    arr = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr.append((i,j))
    return arr

def print_board(queens,n):
    for i in range(n):
        for j in range(n):
            if (i+1,j+1) in queens:
                print("Q",end=" ")
            else:
                print(".",end=" ")
        print("")
    print("\n")    

def possible(board,queen):
    out = board[:]
    (x,y) = queen
    for i in range(1,n+1):
      #Rook conditions
        if (x,i) in out:
            out.remove((x,i))
        if (i,y) in out:
            out.remove((i,y))
        check_list = [(i,i),(i,-i),(-i,i),(-i,-i)]
      #Bishop conditions
        for (p,q) in check_list:
          if (x+p,y+q) in out:
            out.remove((x+p,y+q))
    return out
    
def n_queen(board,queens,row):
    global n
    if len(queens) == n:
        print_board(queens,n)
        global count
        count += 1
        return None
    for column in range(1,n+1):
        tmp = board[:]
        if (row,column) in board:
          queens.append((row,column))
          board = possible(board,(row,column))
          n_queen(board,queens,row+1)
        board = tmp
        if (row,column) in queens:
            queens.remove((row,column))

print("Problem 2")
print("Part 1")      
n_queen(generate(n),[],1)
print(count)

#Part 2
#Superqueen problem (Really inefficient approach. Takes long time to compute for n > 10)
def generate(n):
    arr = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            arr.append((i,j))
    return arr

def print_board(queens,n):
    for i in range(n):
        for j in range(n):
            if (i+1,j+1) in queens:
                print("Q",end=" ")
            else:
                print(".",end=" ")
        print("")
    print("\n")    

def possible(board,queen):
    out = board[:]
    (x,y) = queen
    for i in range(1,n+1):
      #Rook conditions
        if (x,i) in out:
            out.remove((x,i))
        if (i,y) in out:
            out.remove((i,y))
        check_list = [(i,i),(i,-i),(-i,i),(-i,-i)]
      #Bishop conditions
        for (p,q) in check_list:
          if (x+p,y+q) in out:
            out.remove((x+p,y+q))
    #Knight condition
    knight_list = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
    for (a,b) in knight_list:
      if (x+a,y+b) in out:
        out.remove((x+a,y+b))
    return out

def n_queen(board,queens,row,h):
    global n
    if len(queens) == h:
        global flag
        flag = True
        return 
    if row > n:
        return
        
    for column in range(1,n+1):
        tmp = board[:]
        if (row,column) in board:
          queens.append((row,column))
          board = possible(board,(row,column))
        n_queen(board,queens,row+1,h)
        if not flag:
          board = tmp
          if (row,column) in queens:
              queens.remove((row,column))   
print("Part 2")
n = 6
for g in range(n,0,-1):
    flag = False
    n_queen(generate(n),[],1,g)
    if flag:
        print(g)
        break
print()

#Problem 3
def F(L1,L2):
    diff = 0
    for i in L1: diff += i
    for j in L2: diff -= j
    return diff
def oddOne(arr,start,stop):
    if stop-start == 3:
        for i in range(3):
            if arr[start+i] == 2:
                return start+i
    x1 = (stop-start)//3
    x2 = 2*(stop-start)//3
    diff = F(arr[0:x1],arr[x1:x2])
    if diff == 0:
        return oddOne(arr,x2,stop)
    elif diff > 0:
        return oddOne(arr,start,x1)
    else:
        return oddOne(arr,x1,x2)

List1 = [1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
List2 = [1,2,1,1,1,1,1,1,1]

print("Problem 3")
print(oddOne(List1,0,len(List1)))
print(oddOne(List2,0,len(List1)))


#Problem 4
class course:
    def __init__(self,instructors,prerequisite,grade):
        self.instructors = instructors
        self.prerequisite = prerequisite
        self.grade = grade
    def result(self):
        if self.grade >= 3:
            print("You have cleared the course")
        else:
            print("You have failed the course")
print("Problem 4")
cs141 = course(["Subhankar Mishra"],[],10)
cs142 = course(["Abhishek Sahu","Abhranil Chatterjee"],[cs141],8)
cs141.result()
cs142.result()