# WAP to find out the factors of all the numbers between two entered numbers 

a = int(input("Enter first number :"))
b = int(input("Enter secound number :"))

for i in range(a+1,b) :
  print(f"Factore of {i} is ",end="")
  for j in range(1,(i//2)+1) :
    if i % j == 0 :
      print(j,end=" ")
  print(f"{i}")
  
