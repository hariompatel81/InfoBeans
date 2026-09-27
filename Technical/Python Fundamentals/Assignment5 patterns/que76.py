'''
x 
xx 
xxx 
xxxx 
xxx 
xx 
x 
'''

# n = int(input("Enter a number :"))
# for i in range(1,n+n) :
#   if i <= n : 
#     for j in range(i) :
#       print("X",end="")
#   else :
#     for j in range(n+n-i,0,-1) :
#       print("X",end="")
#   print()

n = int(input("Enter a number:"))
for i in range(1,n+1) :
  for j in range(i) :
    print("X",end="")
  print()

for i in range(n-1,0,-1) :
  for j in range(i) :
    print("X",end="")
  print()
