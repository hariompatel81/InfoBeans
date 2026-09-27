# 1	9	25	49	81	….. 
n = int(input("Enter a number :"))
nth = 0
i = 1
x = n
while x > 0 :
  if i % 2 != 0 :
    nth = i*i
    x -= 1
    print(nth,end=" ")
  i += 1

print(f"\n{n}th term is {nth}")






