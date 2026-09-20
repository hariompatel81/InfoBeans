#  8) WAP to print Fibonacci series.

n = int(input("How much number do you want of fibonacci series : "))

a = 0
b = 1

if n < 1 :
  print("Invalid number!")
else :
  for _ in range(n):
    print(f"{a}",end=" ")
    c = a+b
    a = b
    b = c
    
  