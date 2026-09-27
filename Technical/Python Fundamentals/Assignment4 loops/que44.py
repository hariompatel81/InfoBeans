# WAP to find out HCF of a number 

a = int(input("Enter a number :"))
b = int(input("Enter a number :"))

if a > b :
  min = b
else :
  min = a

for i in range(1,min+1) :
  if a % i == 0 and b % i == 0 :
    hcf = i

print(f"HCF of {a,b} is {hcf}") 


