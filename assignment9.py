from tabulate import tabulate

#Problem 1

class item:
  def __init__(self,key,value):
    self.key = key
    self.value = value

  def keyHash(self,m=20):
    return hash(self.key)%m

# Creating objects

names = ["Alice","Bob","Carol","Chuck","Dave","Erin","Eve","Faythe","Frank","Grace","Heidi","Ivan","Judy","Mallory","Mike","Olivia","Oscar","Peggy","Rupert","Trudy","Walter","Wendy"]
marks = [12,13,15,20,10,9,20,24,19,18,11,14,14,16,18,14,12,23,22,19,22,18]

for i in range(len(names)):
  exec(f"item{i} = item('{names[i]}',{marks[i]})")

# Problem 2

class hashTable:
  def __init__(self,m=20):
    self.memory = [[] for i in range(m)]
  
  def __getitem__(self,key):
    index = hash(key)%(len(self.memory))
    for i in self.memory[index]:
      if i.key == key:
        return i.value
    return "Item not found!"

  def __setitem__(self,key,newvalue):
    index = hash(key)%(len(self.memory))
    for i in self.memory[index]:
      if i.key == key:
        i.value = newvalue
        return "Item updated!"
    self.memory[index].append(item(key,newvalue))
    return "Item added!"
  
  def insert(self,item):
    index = item.keyHash()
    self.memory[index].append(item)
    return "Item added!"
  
  def __delitem__(self,key):
    for i in self.memory:
      for j in i:
        if j.key == key:
          i.remove(j)
          return "Removed!"
    return "Item not found"

  def __str__(self):
    data = ["" for i in range(len(self.memory))]
    for i in range(len(self.memory)):
      for j in self.memory[i]:
        data[i]+=f" ({j.key}:{j.value}) "
    out  = [[i,data[i]] for i in range(len(self.memory))]
    return tabulate(out,headers=["Hash","Items"],tablefmt="grid")
  
# Creating a hashTable

table = hashTable()

# Inserting items

for i in range(len(names)):
  exec(f"table.insert(item{i})")

print("Before Operations: ")
print()
print(table)

# Operations

table["Chad"] = 7
table["Niaj"] = 25
table["Bob"] = 22
del table["Peggy"]

print(f"table[Trudy'] = {table['Trudy']}")

print("After Operations: ")
print()
print(table)