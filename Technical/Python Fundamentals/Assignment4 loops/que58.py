# WAP to print all the prime numbers between two entered numbers 

a = int(input("Enter first number :"))
b = int(input("Enter secound number :"))

print("Prime numbers ")
for i in range(a+1,b) :
  prime = True
  for j in range(2,(i//2)+1) :
    if i%j == 0 :
      prime = False
      break

  if prime :
    print(i,end=" ")