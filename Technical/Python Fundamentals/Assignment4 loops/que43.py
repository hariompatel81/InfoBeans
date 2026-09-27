# WAP to find out LCM of a number 

a = int(input("Enter a first number :"))
b = int(input("Enter a secound number :"))

maxitem = max(a,b)

while True :
  if maxitem % a == 0 and maxitem % b == 0 :
    break
  maxitem += 1

print(f"LCM of {a,b} is {maxitem}")
