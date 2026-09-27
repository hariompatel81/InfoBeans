# WAP to print all the strong numbers between two entered numbers 

a = int(input("Enter first number :"))
b = int(input("Enter secound number :"))
print("Strong number is :",end=" ")

for i in range(a+1,b) :
  sum = 0
  x = i
  while x :
    fact = 1
    rem = x % 10
    for j in range(2,rem+1) :
      fact = fact * j
    sum += fact
    x //= 10

  if sum == i :
    print(i,end=" ")
    


