'''
* 
** 
**** 
******* 
*********** 
'''

# x = 0
# for i in range(1,6) :
#   if i < 3 :
#     for j in range(i) :
#       print("*",end="")
#   else :
#     for j in range(i+(3*x)) :
#       print("*",end="")
#     x += 1
#   print()

n = int(input("Enter a number :"))
start = 1;
end = 0;
for i in range(n) :
  start += end
  for j in range(start) :
    print("*",end="")
  end += 1
  print()
