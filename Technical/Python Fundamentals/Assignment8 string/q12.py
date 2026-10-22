# 12. Check whether two strings are equal without using == for the complete strings.

s1 = "nitin"
s2 = "Nitin"

i =0
if len(s1) - len(s2):
  print("Not equal")
else :
  for i in range(len(s1)) :
    if ord(s1[i]) - ord(s2[i]) :
      print("Not equal")
      break
  else :
    print("equal")
  



  

  
