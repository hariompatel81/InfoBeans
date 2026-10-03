# find pick element
arr = [2,3,4,2,5,5,7,3,6,4,6,4,6]

if len(arr)==1 or arr[len(arr)-1] > arr[len(arr)-2] :
  print("1")
else :
  for i in range(len(arr)-1) :
    if i==0 and arr[i] > arr[i+1] :
      print("1")
      break
    elif (arr[i] > arr[i+1]) and (arr[i] > arr[i-1]) :
      print("1")
      break
  else :
      print("0")
