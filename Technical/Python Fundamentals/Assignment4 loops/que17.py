# 17) 1 	2	 4	 7	 11	 16 	…… n terms

n = int(input("Enter a number :"))
n_term = 1
print("Series :",end="")
for i in range(1,n) :
  print(n_term,end=" ")
  n_term += i
  
print(n_term)
print(f"{n}th term is : {n_term}")
