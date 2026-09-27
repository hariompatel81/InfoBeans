# WAP to print all the even numbers between two entered numbers 
a = int(input("Enter first number :"))
b = int(input("Enter secound number :"))

print("Even numbers are :",end=" ")
for i in range(a+1,b) :
  if i % 2 == 0 :
    print(i,end=" ")

