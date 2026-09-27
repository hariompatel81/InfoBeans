# 0	4	16	36	64	….. 

n = int(input("Enter a number :"))
diff = 4
nth = 0
for _ in range(n) :
  print(nth,end=" ")
  temp = nth
  nth += diff
  diff += 8
print(f"\n{n}th term is {temp}")    