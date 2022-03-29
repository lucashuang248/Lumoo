matrix = []
for i  in range (1):

  matrix.append([])
  for j in range (1,5):
    matrix [i].append(j)

matrix2 = []
for i in range (1):
  matrix2.append([])
  for k in range (5,10):
    matrix2 [i].append(k)

matrix3 = []
for i in range (1):
  matrix3.append ([])
  for g in range (10,15):
    matrix3 [i].append(g)

matrix4 = []
for i in range (1):
  matrix4.append ([])
  for h in range (15,20):
    matrix4 [i].append(h)

print(matrix)
print(matrix2)
print(matrix3)
print(matrix4)

def print_matrix1(matrix):
  print("hehe")
  for i in range(len(matrix)): 
    for j in range(len(matrix[i])):
      print(matrix[i][j], end=" ")
    print()