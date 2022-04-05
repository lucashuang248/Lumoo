RESET_COLOR = u"\u001B[0m\u001B[2D"

def hi():
  n = int(input('Hi:'))
  
  counter = 0
  
  while counter < n:
      print("\033[1;32;32m Hi  \n")
      counter = counter + 1
  else:
      print("\033[1;32;31m Bye  \n")

  print(RESET_COLOR)

