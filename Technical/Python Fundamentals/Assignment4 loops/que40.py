# A b C d E f G h …… n terms  
n = int(input("Enter a number :"))
for i in range(1,n+1) :
  if i%2!=0:
    print(chr(64+i),end=" ")
  else :
    print(chr(96+i),end=" ")