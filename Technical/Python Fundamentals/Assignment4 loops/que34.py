# 0 8 64 216 ………… 
n = int(input("Enter a number :"))
i = 0
x = n
while n > 0 :
  if i % 2 == 0 :
    nth = i**3
    print(nth,end=" ")
    n -= 1
  i += 1

print(f"\n{x}th term is {nth}")