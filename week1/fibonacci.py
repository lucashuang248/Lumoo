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