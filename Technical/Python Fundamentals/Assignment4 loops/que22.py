# 1	8	27	64	125	….. 
n = int(input("Enter a number :"))
nth = 0
for i in range(1,n+1) :
  nth = i**3
  print(nth,end=" ")

print(f"\n{n}th term is {nth}")
