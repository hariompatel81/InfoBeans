# WAP to find out all the palindrome numbers between two entered numbers  
a = int(input("Enter first number :"))
b = int(input("Enter secound number :"))

print("Pelindrom no. is :",end=" ")
for i in range(a+1,b) :
  n = i
  rev = 0
  while n :
    rem = n % 10
    rev = rev*10 + rem
    n //= 10
  if i == rev :
    print(i,end=" ")
  
