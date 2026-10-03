# WAP to print all the alphabets in pattern according to the selected case using switch case. 

ch = input("Enter any cherecter in uppercase :")
n = 10
match ch :
  case "A" :
    for i in range(1,(n//2)+1) :
      for j in range(1,n) :
        if i+j == (n//2)+1 or (i == 3 and (j>2 and j<8)) or (j>5 and (i+j == j*2-4)) :
          print("*",end="")
        else :
          print(" ",end="")
      print()

  case "B":
    for i in range(1,10) :
      for j in range(1,(n//2)+1) :
        if j == 1 or (i == 1 and j<(n//2)) or (i == n//2 and j<n//2) or (i==n-1 and j < n//2) or (j==n//2 and (i>1 and i<n//2) or (j==5 and (i>n//2 and i<n-1))) :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "C" :
    for i in range(1,(n//2)+1) :
      for j in range(1,(n//2)+1) :
        if (j==1 and (i>1 and i<(n//2))) or (i==1 and j>1) or (i==(n//2) and j>1) :
          print("*",end=" ")
        else :
          print(" ",end="")
      print()

  case "D" :
    for i in range(1,(n//2)+1) :
      for j in range(1,(n//2)+1) :
        if j == 1 or (i==1 and j<(n//2)) or (i==(n//2) and j<(n//2)) or (j==(n//2) and (i>1 and i<(n//2))) :
          print("*",end=" ")
        else :
          print(" ",end=" ") 
      print()

  case "E" :
    for i in range(1,n) :
      for j in range(1,(n//2)+1) :
        if j==1 or i==1 or i==((n//2)) or i==n-1 :
          print("*",end=" ")
        else :
          print(" ",end="")
      print()

  case "F" :
    for i in range(1,n) :
      for j in range(1,(n//2)+1) :
        if i==1 or j==1 or i==(n//2) :
          print("*",end=" ")
      print()

  case "G" :
    for i in range(1,(n//2)+1) :
      for j in range(1,(n//2)+1) :
        if (i==1 and (j>1 and j<(n//2))) or (j==1 and (i>1 and i < (n//2))) or (i==n//2 and j>1) or (i==1 and j==n//2) or(i==3 and j>2) or (i==4 and j==n//2):
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "H" :
    for i in range(1,(n//2)+1) :
      for j in range(1,(n//2)+1) :
        if j==1 or j==n//2 or i==3 :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "I" :
    for i in range(1,(n//2)+1) :
      for j in range(1,(n//2)+1) :
        if i==1 or i==(n//2) or j==3 :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "J" :
    for i in range(1,(n//2)+1) :
      for j in range(1,n) :
        if i==1 or (j==n//2 and i < n//2) or (i==n//2 and (j>1 and j<n//2)) or (j==1 and i==4) :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()  

  case "K" :
    temp = 2
    for i in range(1,n) :
      for j in range(1,(n//2)+1) :
        if j==1 or i+j == 6 or (i>n//2 and i-j == 4) :
          print("*",end=" ")
          
        else :
          print(" ",end=" ")

      print()

  case "L" :
    for i in range(1,n) :
      print("*")
      if i == n-1 :
        for _ in range(n//2) :
          print("*",end=" ")
    print()

  case "M" :
    for i in range(1,(n//2)+1) :
      for j in range(1,(n//2)+1) :
        if j==1 or j == n//2 or (i<4 and (i==j or i+j==6)) :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "N" :
    for i in range(1,(n//2)+1) :
      for j in range(1,(n//2)+1) :
        if j==1 or j==n//2 or i==j :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "O" :
    for i in range(1,(n//2)+1) :
      for j in range(1,(n//2)+1) :
        if ((i==1 or i==5) and (j>1 and j<n//2)) or ((j==1 or j==n//2) and (i>1 and i<n//2)):
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "P" :
    for i in range(1,n) :
      for j in range(1,(n//2)+1) :
        if j==1 or ((i==1 or i == 5) and (j<n//2)) or (j==n//2 and (i>1 and i<n//2)) :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "Q" :
    for i in range(1,(n//2)+3) :
      for j in range(1,(n//2)+1) :
        if ((i==1 or i==n//2) and (j>1 and j<n//2)) or ((j==1 or j==n//2) and (i>1 and i<n//2)) or (i==(n//2)+1 and j==(n//2)-1) or (i==(n//2)+2 and j==n//2):
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "R" :
    for i in range(1,n) :
      for j in range(1,(n//2)+1) :
        if j==1 or (i==1 and j<n//2) or (j==n//2 and (i>1 and i<n//2)) or (i==n//2 and (j<n//2)) or i-j==4 :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "S" :
    for i in range(1,n) :
      for j in range(1,(n//2)+1) :
        if ((i==1 or i==n//2 or i==n-1) and (j>1 and j<n//2)) or (j==1 and (i>1 and i<n//2 or i==8) or (j==n//2 and (i>n//2 and i<n-1 or i==2))) :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "T" :
    for i in range(1,(n//2)+1) :
      for j in range(1,(n//2)+1) :
        if i==1 or j==3 :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "U" :
    for i in range(1,(n//2)+1) :
      for j in range(1,(n//2)+1) :
        if ((j==1 or j==n//2) and (i<n//2)) or (i==n//2 and (j>1 and j<n//2)) :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "V" :
    for i in range(1,(n//2)+1) :
      for j in range(1,n) :
        if i==j or i+j==10 :
          print("*",end="")
        else :
          print(" ",end="")
      print()

  case "W" :
    for i in range(1,(n//2)+1) :
      for j in range(1,(n//2)+1) :
        if j==1 or j==n//2 or (i>2 and (i==j or i+j==6)) :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "X" :
    for i in range(1,(n//2)+1) :
      for j in range(1,(n//2)+1) :
        if i==j or i+j == 6 :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "Y" :
    for i in range(1,(n//2)+1) :
      for j in range(1,(n//2)+1) :
        if (i<4 and (i==j or i+j==6)) or (i>3 and j==3) :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case "Z" :
    for i in range(1,(n//2)+1) :
      for j in range(1,(n//2)+1) :
        if i==1 or i==n//2 or i+j==6 :
          print("*",end=" ")
        else :
          print(" ",end=" ")
      print()

  case _ :
    print("Invalid input.")