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

  
  