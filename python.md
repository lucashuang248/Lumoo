{% include navigation.html %}

<iframe frameborder="0" width="100%" height="600px" src="https://replit.com/@lucashuang248/Lumoo?embed=true"></iframe>

Week 1 Code Snippets

InfoDB Lists and Loops
```html
InfoDb = []
InfoDb.append({
#list
 "Name": "Lucas Huang",
 "Birthday": "August 28",
 "Siblings": "Yes",
 "Hobbies":["Basketball”, “Eating”, “Listening to Music”, “Playing Video and Board Games"]
})
InfoDb.append({
 "Name": "Timmy Lin",
 "Birthday": "November 10",
 "Siblings": "Yes",
 "Hobbies":["Video Games”, “Pokemon GO”, “Math”,“Snowboard"]
})
def print_data(n):
    print(InfoDb[n]["Name"], InfoDb[n]["Birthday"], InfoDb[n]["Siblings"])
    print("\t", "Hobbies: ", end="")
    print(", ".join(InfoDb[n]["Hobbies"]))
    print()
#for loop
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
#while loopp
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
#recursive loop
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return
#prints the loops
def tester():
    print("For loop:")
    for_loop()
    print("While loop:")
    while_loop(0)
    print("Recursive loop:")
    recursive_loop(0)
```

Fibonacci
```html
try:
  num = int(input("Input number: "))
  assert num > 0
  n1, n2 = 0, 1
  print("Fibonacci Series: ", n1, n2, end=" ")
  for int in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")
  print()
except AssertionError :
  print("can't have a negative value")
```


Week 0 Code Snippets

Christmas Tree
```html
def triangleShape(n):
  for i in range(n):
      for j in range(n-i):
          print(' ', end=' ')
      for k in range(2*i+1):
          print('*',end=' ')
      print()
  
  # Generating recatngle shape
def rectangleshape(n):
  for i in range(n):
      for j in range(n-1):
          print(' ', end=' ')
      print('* * *')
    
def treeprint():
  row = int(input('Enter number of rows: '))
  triangleShape(row)
  triangleShape(row)
  rectangleshape(row)
```


Matrix Number Pad
```html
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
```
