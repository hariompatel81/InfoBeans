# 0 7 14 21 28 35 …..n

nth = 0
n = int(input("Enter a number :"))
for i in range(n) :
  nth = 7*i
  print(nth,end=" ")

print()
print(f"{n}th term is {nth}")
