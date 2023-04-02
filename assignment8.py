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