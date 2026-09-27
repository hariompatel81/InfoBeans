# 1 2 2 4 8 32 …… n terms

n = int(input("Enter a number :"))
a = 1
b = 2
if n==1 :
  print(f"{n}th term is {a}")
else :
  print(f"Series is {a}",end=" ")
  for i in range(n-1) :
   k = a*b
   a = b
   b = k
   print(f"{a}",end=" ")

print()
print(f"{n}th term is {a}")


