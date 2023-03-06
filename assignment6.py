given = {(0,6):2 , (1,1):8, (1,5):7, (1,7):9,(2,0):6 , (2,2):2, (2,6):5, (3,1):7 , (3,4):6, (4,3):9 ,(4,5):1, (5,4):2 , (5,7):4, (6,2):5 , (6,6):6 ,(6,8):3, (7,1):9 , (7,3):4, (7,7):7 , (8,2):6 }

def generate(given):
  out = []
  for i in range(9):
    aux = []
    for j in range(9):
      if (i,j) in given:
        aux.append(given[(i,j)])
      else:
        aux.append(".")
    out.append(aux)
  return out

def pretty_print(board):
  print("+-"*10+"+")
  for i in board:
    print("| ",end="")
    for j in i:
      print(j,end=" ")
    print("|")
  print("+-"*10+"+")

board = generate(given) 

def possible(board,position,num):
  (x,y) = position
  if board[x][y] != ".":
    return False
  for a in range(9):
    if board[x][a] == num:
      return False
    if board[a][y] == num:
      return False
  (m,n) = (x-(x%3),y-(y%3))
  for p in range(m,m+3):
    for q in range(n,n+3):
      if board[p][q] == num:
        return False
  return True


def find(board):
  i = j = 0
  while i<9:
    if board[i][j] == ".":
      return (i,j)
    if j+1 == 9:
      j = 0
      i += 1
    else:
      j += 1


def solve(board):
  position = find(board)
  if not position:
    pretty_print(board)
    return True
  else:
    (x,y) = position
  for i in range(1,10):
    if possible(board,position,i):
      board[x][y] = i
      if solve(board):
        return True
      board[x][y] = "."
  return False
solve(board)
