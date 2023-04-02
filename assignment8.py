# Problem 1
class Node:
  def __init__(self,data,left=None,right=None):
    self.data = data
    self.left = left
    self.right = right

class Tree:
  def __init__(self,root):
    self.root = root
  def inorderPrint(self,root=False):
    if root is False:
      root = self.root
    if root != None:
      self.inorderPrint(root=root.left)
      print(root.data,end="  ")
      self.inorderPrint(root=root.right)

# Creating nodes
nodes = [2,7,5,2,6,9,5,11,4]
for i in range(9):
  exec(f"node{i+1}=Node('{nodes[i]}')")

#Creating Tree
binTree = Tree(node1)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node5.left = node7
node5.right = node8
node3.right = node6
node6.left = node9

print("[Problem 1]")

binTree.inorderPrint()
print()

# Problem 2

def evaluate(BinTree,node):
  if (node.left or node.right) == None:
    return node.data

  left = int(evaluate(BinTree,node.left))
  right = int(evaluate(BinTree,node.right))

  if node.data == "+":
    return left + right
  elif node.data == "-":
    return left - right
  elif node.data == "x":
    return left * right
  elif node.data == "/":
    return left / right

def GenerateTree(BinTree,Expression,node):
  if node == None:
    node = Node("None")
    BinTree.root = node

  if len(Expression) == 1:
    node.data = (Expression[0])
    return 

  mid = findOperator(Expression)
  node.data = Expression[mid] 
  node.left = Node("None")   
  node.right = Node("None")

  GenerateTree(BinTree,Expression[1:mid],node.left)
  GenerateTree(BinTree,Expression[mid+1:-1],node.right)

def findOperator(Expression):
  left = right = 0
  for i in range(1,len(Expression)-1):
    if Expression[i] == "(":
      left += 1
    if Expression[i] == ")":
      right += 1
    if left == right:
      return i + 1
  for i in range(len(Expression)):
    if Expression[i] in '+-x/':
      return i
  return -1

BinTree = Tree(None)

print("[Problem 2]")

GenerateTree(BinTree,[*"(((3+5)x7)+5)"],BinTree.root)

print("Binary Tree: ",end="")
BinTree.inorderPrint()
print()

print(f"Output - {evaluate(BinTree,BinTree.root)}")
