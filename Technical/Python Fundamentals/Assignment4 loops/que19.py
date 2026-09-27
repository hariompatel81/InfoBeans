# 1	+	1/2	+	1/3	+	1/4	+	1/5	….. n terms(find out sum) 

n = int(input("Enter a number :"))
sum = 0
for i in range(1,n+1) :
  sum += 1/i
  print(f"1/{i}",end=" + ")
print()
print(f"sum of {n}th term is {sum:.2f}")  