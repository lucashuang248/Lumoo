{% include navigation.html %}

<iframe frameborder="0" width="100%" height="600px" src="https://replit.com/@lucashuang248/Lumoo?embed=true"></iframe>

# Week 3 Code Snippets & Key Learnings
### Palindrome
```html
class palindrome:
    def __init__(self):
        self.s = ""

    def palincheck(self):
        x = "palindrome"

        w = ""
        for i in x:
            w = i + w

        if (x == w):
            print("\nIt's a palindrome!")
        else:
            print("\nNah this isn't a palindrome")

    def palincheck2(self):
        y = "A man, the plan, the moon"
        w = ""
        for i in y:
            w = i + w
        if (y == w):
            print("\nIt's a palindrome!")
        else:
            print("\nNah this isn't a palindrome")

    def palincheck3(self):
        y = "racecar"
        w = ""
        for i in y:
            w = i + w
        if (y == w):
            print("\nIt's a palindrome!")
        else:
            print("\nNah this isn't a palindrome")
```
```html
PALIN = palindrome()
print("\nChecking if 'palindrome' is a palindrome... : ")
print(PALIN.palincheck())
print("\nChecking if 'A man, the plan, the moon' is a palindrome... : ")
print(PALIN.palincheck2())
print("\nChecking if 'racecar' is a palindrome...: ")
print(PALIN.palincheck3())
print("-------------------------------")

```
### Name
```html
def name(n):
  for s in range(n):
      for l in range(n-2):
          print(' ', end=' ')
      print('(っ◔◡◔)っ ♥ I love Samuel ♥')

def nameprint():
  row = int(input('rows:'))
  name(row)
```

# Week 2 Code Snippets

### Factorial
```html
class Fibonacci:
    def __init__(self):
        self.fiboSeq = [0, 1]


    def __call__(self, n):
        if n < len(self.fiboSeq):
            return self.fiboSeq[n]
        else:
            # Compute the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2) # two recursive calls to self (__call__(self, n))
            self.fiboSeq.append(fib_number) # builds list, with most nested of the calculations 1st... may hurt your head
        return self.fiboSeq[n]

fiboans = int(input("Choose a number "))
fibo_of = Fibonacci() # object instantiation and run __init__ method
print("\nFactorial is : ")
print(fibo_of(fiboans)) # object running __call__ method

print("\nFactorial of 29 is : ")
print(fibo_of(29))
```

### Palindrome
```html
class palindrome:
  def __init__(self):
    self.s = ""
    

  def palincheck(self):
    x = "palindrome"
 
    w = ""
    for i in x:
        w = i + w
     
    if (x == w):
        print("\nIt's a palindrome!")
    else:
        print("\nNah this isn't a palindrome")

  def palincheck2(self):
    y = "A man, the plan, the moon"
    w = ""
    for i in y:
      w = i + w
    if (y == w):
        print("\nIt's a palindrome!")
    else:
      print("\nNah this isn't a palindrome")

  def palincheck3(self):
    y = "racecar"
    w = ""
    for i in y:
      w = i + w
    if (y == w):
        print("\nIt's a palindrome!")
    else:
      print("\nNah this isn't a palindrome")

PALIN = palindrome()
print("\nChecking if 'palindrome' is a palindrome... : ")
print(PALIN.palincheck())
print("\nChecking if 'A man, the plan, the moon' is a palindrome... : ")
print(PALIN.palincheck2())
print("\nChecking if 'racecar' is a palindrome...: ")
print(PALIN.palincheck3())
print("-------------------------------")
```

### Math Function

```html
#Writing in Imperative here
print("-------------------------------")
print("\nStart of Imperative Programming of GCD Function")
def findgcd(num1, num2):
    if num1 == 0:
        return num1
    while num2 != 0:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

ans = findgcd(18, 200)
print("\nThe GCD of 18 and 200 is..")
print(ans)
print("-------------------------------")



#Writing in OOP here
print("\nStart of OOP Programming of GCD Function")
class findgcd:
  def __init__(self, num1, num2):
    self.num1 = 18
    self.num2 = 200
    

  def findgcdfunc(self, num1, num2):
    if self.num1 == 0:
        return self.num1
    while self.num2 != 0:
        if self.num1 > self.num2:
            self.num1 = self.num1 - self.num2
        else:
            self.num2 = self.num2 - self.num1
    return self.num1

oop = findgcd(18, 200)
print("\nFinding the GCD of 18 and 200... : ")
print(oop.findgcdfunc(18, 200))
print("-------------------------------")
```

# Week 1 Code Snippets

### InfoDB Lists and Loops
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

### Fibonacci
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


# Week 0 Code Snippets

### Christmas Tree
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


### Matrix Number Pad
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

### Animation
```html
import time

ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
SMOKE_COLOR = u"\u001B[40m\u001B[2D"
RED_COLOR = u"\u001B[31m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"


def black_print():
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(SMOKE_COLOR + "  " * 35)
  
def animation_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "  _/---\_   ")
    print(sp + " /  . .  \   ")
    print(sp + " |   <   |   ")
    print(sp + " \ |___| / ")
    print(sp + "  \_____/  ")
    print(RED_COLOR, end="")
    print(sp + "    | |  ")
    print(RESET_COLOR)

def animation():
    black_print()
  
    start = 0
    distance = 60
    step = 2 

    for position in range(start, distance, step):
        animation_print(position)
        time.sleep(.1)
```

### Ageswap
```html


age1 = float(input("Choose first age: "))
age2 = float(input("Choose second age: "))

if age1 < age2:
    print(age1, age2)
else:
    print(age2, age1)
```
