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