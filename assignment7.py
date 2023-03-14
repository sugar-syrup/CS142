#Problem 1

class Node:
    def __init__(self,alpha,num,next=None):
        self.alpha = alpha
        self.num = num
        self.next = next
    def print_node(self):
        print((self.alpha,self.num))


class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def print_list(self):
        current = self.head
        while current != None:
            print(f"({current.alpha} {current.num}) -> ",end="")
            current = current.next
        print("None")

    def insertAtStart(self,new):
        new.next = self.head
        self.head = new

    def insertAtEnd(self,new):
        if self.head == None:
            self.head = new
            return 
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new
    
    def deleteAtStart(self):
        if self.head == None:
            return
        new_start = self.head.next
        self.head = new_start

    def deleteAtEnd(self):
        if self.head == None:
            return
        current = self.head
        if current.next == None:
            self.head = None
            return
        while current.next.next != None:
            current = current.next
        current.next = None

# Creating a Linked List

n1 = Node("c",1)
n2 = Node("i",7)
n3 = Node("v",3)
n4 = Node("i",2)
n5 = Node("c",8)
n6 = Node("a",7)
n7 = Node("f",6)
n8 = Node("z",12)

l1 = LinkedList()
l1.insertAtStart(n2)
l1.insertAtStart(n1)
l1.insertAtEnd(n3)
l1.insertAtEnd(n4)
l1.insertAtEnd(n5)
l1.insertAtStart(n6)
l1.insertAtStart(n7)
l1.insertAtEnd(n8)

print("[Problem 1]")
l1.print_list()

# Problem 2

def insertToLink(Linked_List:LinkedList,alpha,num):
    node = Node(alpha,num)
    Linked_List.insertAtStart(node)

def Palindrome(Linked_List:LinkedList):
    reverse = LinkedList()
    current = Linked_List.head
    while current != None:
        insertToLink(reverse,current.alpha,current.num)
        current = current.next
    current = Linked_List.head
    reverse_Point = reverse.head
    while current != None:
        if reverse_Point.alpha != current.alpha:
            return False
        current = current.next
        reverse_Point =reverse_Point.next
    return True

print("[Problem 2]")
print(Palindrome(l1))

# Problem 3 

def appendToLink(Linked_List:LinkedList,alpha,num):
    node = Node(alpha,num)
    Linked_List.insertAtEnd(node)
       
def cut_at_centre(Linked_List:LinkedList):
    current = mid = Linked_List.head
    count = 0
    while current != None:
        if count == 2:
            count = 0
            mid = mid.next
        current = current.next
        count += 1
    mid = mid.next
    out2 = LinkedList(mid)
    current = Linked_List.head
    while current.next != mid:
        current = current.next
    current.next = None
    return (Linked_List,out2)

def merge_sort(Linked_List:LinkedList):

    if Linked_List.head == None or Linked_List.head.next == None:
        return Linked_List

    (left_li,right_li) = cut_at_centre(Linked_List)

    left = merge_sort(left_li) 
    right = merge_sort(right_li)


    return merge(left,right)

def merge(left,right):
    empty_list = LinkedList()
    
    leftCurr = left.head
    rightCurr = right.head

    while leftCurr != None and rightCurr != None:
        if leftCurr.num < rightCurr.num:
            appendToLink(empty_list,leftCurr.alpha,leftCurr.num)
            leftCurr = leftCurr.next
        else:
            appendToLink(empty_list,rightCurr.alpha,rightCurr.num)
            rightCurr = rightCurr.next
    
    if leftCurr != None:
        empty_list.insertAtEnd(leftCurr)
    else:
        empty_list.insertAtEnd(rightCurr)
    return empty_list

print("[Problem 3(b)]- Merge sort")
merge_sort(l1).print_list()

